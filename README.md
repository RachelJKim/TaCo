# TaCo: Taxel-based Color Representation Library
TaCo provides functionality for representing colors using symbols called "**Taxels**" and generating SVG files containing color grids or images composed of multiple Taxels.

---

## Introduction
The TaCo library aims to provide a unique way of representing colors using symbols called "Taxels" for blinds. A Taxel is a graphical representation of a color based on its HSV (Hue, Saturation, Value) components. This allows you to generate SVG files containing color grids or images composed of multiple Taxels.

The main features of the TaCo include:
1. Representing colors using Taxels
2. Generating color grids with various color schemes
3. Creating SVG files containing Taxels and color grids
4. Providing a set of predefined color palettes (e.g., PANTONE colors)

## Usage
Here's a basic example of how to use the TaCo library:

```Python
from taco import color, SVG, Canvas

# Create a color using HSV values
my_color = color(180, 50, 80)   #(h,s,v) = (180,50,80)

# Create a canvas
canvas = Canvas(100, 100)

# Add a Taxel representing the color to the canvas
canvas.add(SVG.taxel(10, 10, my_color))

# Save the SVG file
canvas.save("output.svg")
```
In this example, we create a color using HSV values, create a canvas, add a Taxel representing the color to the canvas in (10,10), and save the SVG file as `output.svg`.

## File Descriptions
The TaCo library consists of the following files:
### main.py
The main.py file serves as the entry point of the library. It demonstrates how to use the TaCo library to generate color grids and SVG files. The file contains code for creating color grids based on different color schemes, such as hue vs. saturation, hue vs. value, and random combinations of HSV values. It also includes an example of generating an SVG file with named colors from the PANTONE color palette.
### palette.py
The palette.py file defines a collection of predefined color palettes, such as the PANTONE color palette. It provides a convenient way to access commonly used colors by their names. The colors are represented using the rgb_to_hsv function from the util.py file.
### taco.py
The taco.py file contains the core functionality of the TaCo library. It defines the *SVG* class, which provides methods for generating SVG elements such as rectangles and Taxels. The *Taxel* class represents a color using a combination of a hueline (representing saturation and hue) and a baseline (representing value). The file also defines the *Canvas* class, which represents an SVG canvas and allows adding SVG elements to it.
### util.py
The util.py file contains utility functions used by the TaCo.
    - function `rgb_to_hsv` | converts an RGB color to its HSV representation.

---

## License
The TaCo library is open-source and released under the MIT License.