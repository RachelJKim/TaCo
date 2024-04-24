from collections import namedtuple

obj = namedtuple('svg', ['src', 'attr'])   # class SVG return type
color = namedtuple('hsv', ['h', 's', 'v']) # HSV color

class SVG:
    """A class for generating SVG elements."""
    
    # Hueline property [mm]
    _HUE_WIDTH: float = 4.5 
    _HUE_HEIGHT: float = 0.6
    _HUE_CORNER_RADIUS: float = _HUE_HEIGHT / 2

    # Baseline property [mm]
    _BASE_WIDTH: float = 4.5
    _BASE_HEIGHT_MIN: float = 0.8
    _BASE_HEIGHT_MAX: float = 4.5
    _BASE_CORNER_RADIUS: float = _BASE_HEIGHT_MIN / 2

    # EPS: small distance between baseline and hueline
    _EPS: float = 0.08

    @staticmethod
    def rect(x: float, y: float, width: float, height: float, rx: int | float = 0,
             rotate: None | tuple[int, int, int] = None) -> obj:
        '''
        Generate an SVG rect element.
        
        Args:
            x (float): The x-coordinate of the top-left corner.
            y (float): The y-coordinate of the top-left corner. 
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
            rx (int | float): The x-axis radius for rounded corners (default 0).
            rotate (None | tuple[int, int, int]): Rotation parameters - angle, 
                cx, cy where (cx, cy) is the center of rotation relative to the
                top-left corner of the rectangle (default None).

        Returns:
            obj: An SVG rect element and its attributes.
        '''
        if all(value > 0 for value in [width, height, rx]):
            x, y, width, height, rx = (str(round(val, 3)) for val in [x, y, width, height, rx])
            src = f'<rect x="{x}" y="{y}"\n' \
                  f'      width="{width}" height="{height}"\n' \
                  f'      rx="{rx}"\n'

            if rotate is not None:
                angle, cx, cy = rotate
                src += f'\n      transform="rotate({angle:3} {(float(x) + cx):.3} {(float(y) + cy):.3})"'

                return obj(src + '\n/>',
                           {'x': x, 'y': y, 'width': width, 'height': height, 'corner_radius': rx,
                            'angle': angle, 'cx': cx, 'cy': cy})
            else:
                return obj(src + '\n/>',
                           {'x': x, 'y': y, 'width': width, 'height': height, 'corner_radius': rx})
        else:
            return None

    @staticmethod
    def combine(obj1: obj, obj2: obj) -> str:
        """
        Combine the src attributes of two SVG objects.

        Args:
            obj1 (obj): The first SVG object.
            obj2 (obj): The second SVG object.

        Returns:
            str: The combined src string.
        """
        src1 = obj1.src if obj1 else ""
        src2 = obj2.src if obj2 else ""
        return src1 + "\n" + src2 if src1 and src2 else src1 or src2

    @classmethod
    def taxel(cls, x: float, y: float, hsv: color) -> obj:
        '''
        Generate a taxel SVG element representing a color. 

        Args:
            x (float): The x-coordinate of the top-left corner of the baseline.
            y (float): The y-coordinate of the top-left corner of the baseline.
            hsv (color): The HSV color parameters.

        Returns:
            obj: A taxel SVG element and its attributes.
        '''
        # represents saturation
        hueline_width = hsv.s / 100 * cls._HUE_WIDTH
        # represents hue  
        hueline_angle = hsv.h / 2
        hueline_center_of_rotation = (round(hueline_width - cls._HUE_HEIGHT / 2, 3),
                                      round(cls._HUE_HEIGHT / 2, 3))
        # represents value (more precisely, 100-value)
        baseline_height = cls._BASE_HEIGHT_MIN + (100 - hsv.v) / 100 * (
                cls._BASE_HEIGHT_MAX - cls._BASE_HEIGHT_MIN)

        hueline = cls.rect(x + (cls._HUE_WIDTH - hueline_width), (y - cls._HUE_HEIGHT - cls._EPS),
                           hueline_width, cls._HUE_HEIGHT,
                           cls._HUE_CORNER_RADIUS,
                           (hueline_angle, *hueline_center_of_rotation))
        
        baseline = cls.rect(x, y,
                            cls._BASE_WIDTH, baseline_height, 
                            cls._BASE_CORNER_RADIUS)

        return obj(cls.combine(hueline, baseline),
                   {'x': x, 'y': y, 'color': hsv})


class Canvas:
    """A class representing an SVG canvas."""

    def __init__(self, width: float, height: float, filename='symbol.svg'):
        '''
        Initialize the SVG canvas.

        Args:
            width (float): The width of the canvas in mm.
            height (float): The height of the canvas in mm.
            filename (str): The filename to save the SVG (default 'symbol.svg').
        '''
        self._src = f'<svg xmlns="http://www.w3.org/2000/svg"\n' \
                    f'     width="{width}mm"\n' \
                    f'     height="{height}mm"\n' \
                    f'     viewBox="0 0 {width} {height}">\n'
        self._filename = filename

    @property
    def src(self) -> str:
        '''Get the SVG source with the closing tag.'''
        return self._src + '\n</svg>'

    @property
    def filename(self) -> str:
        '''Get the filename of the SVG.'''
        return self._filename

    @filename.setter
    def filename(self, new_filename):
        '''Set the filename of the SVG.'''
        self._filename = new_filename

    def add(self, obj: obj) -> None:
        '''Add an SVG element to the canvas.'''
        self._src += obj.src

    def save(self):
        '''Save the SVG to a file.'''
        with open(self._filename, 'w') as file:
            file.write(self._src + '\n</svg>')

        print(f"{self._filename} file generated.")