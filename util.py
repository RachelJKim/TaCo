from taco import color

def rgb_to_hsv(r: int, g: int, b: int) -> color:
    '''
    Convert an RGB color to HSV.

    Args:
        r (int): Red component (0-255).
        g (int): Green component (0-255).
        b (int): Blue component (0-255).

    Returns:
        hsv (color): HSV values (H: 0-360, S: 0-100, V: 0-100).
    '''
    # Normalize RGB values to the range [0, 1]
    r, g, b = r / 255, g / 255, b / 255

    # Find the maximum and minimum values of RGB
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    
    # Calculate the value (V)
    v = max_val * 100

    # Calculate the saturation (S)
    if max_val == 0:
        s = 0
    else:
        s = (1 - min_val / max_val) * 100

    # Calculate the hue (H)
    if max_val == min_val:
        h = 0  # Undefined, can be any value
    else:
        if max_val == r:
            h = (60 * (g - b) / (max_val - min_val) + 360) % 360
        elif max_val == g:
            h = 60 * (b - r) / (max_val - min_val) + 120
        else:  # max_val == b
            h = 60 * (r - g) / (max_val - min_val) + 240

    return color(round(h, 2), round(s, 2), round(v, 2))