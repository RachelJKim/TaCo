from random import randint
from taco import color, SVG, Canvas
from palette import PANTONE

PADDING_X, PADDING_Y = 2, 5.5
GRID_X, GRID_Y = 10, 11

if __name__ == '__main__':

    ###### making color grid
    # hue vs saturation
    colors_matrix = [[color(h, s, 100) for h in range(0, 321, 40)] for s in range(20, 101, 20)]
    # hue vs value 
    colors_matrix.extend([[color(h, 100, v) for h in range(0, 321, 40)] for v in range(80, 19, -20)])
    # grey scale add
    colors_matrix = [row + [color(0, 0, v)] for row, v in zip(colors_matrix, range(100, -1, -int(100 / (9 - 1))))]
    # randomly combined (hsv) sample colors
    random_colors_matrix = [[color(h, 20 * randint(1, 5), randint(0, 100)) for h in range(0, 321, 40)] for _ in range(2)] * 2

    canvas = Canvas(2 * PADDING_X + GRID_X * len(colors_matrix[0]), 2 * PADDING_Y + GRID_Y * (len(colors_matrix) + len(random_colors_matrix)))
    canvas.filename = 'src/assets/symbols.svg'

    for row, colors_row in enumerate(colors_matrix):
        for col, color in enumerate(colors_row):
            canvas.add(SVG.taxel(PADDING_X + GRID_X * col, PADDING_Y + GRID_Y * row, color))

    for row, colors_row in enumerate(random_colors_matrix):
        for col, color in enumerate(colors_row):
            canvas.add(SVG.taxel(PADDING_X + GRID_X * col, 4 + PADDING_Y + GRID_Y * (len(colors_matrix) + row), color))
            
    canvas.save()

    ###### making named colors (PANTONE)
    canvas2 = Canvas(50,50)
    canvas2.filename = 'src/assets/card.svg'
    card_colors = [[PANTONE.brightred, PANTONE.orange021, PANTONE.yellow],
                   [PANTONE.green, PANTONE.processblue, PANTONE.blue072],
                   [PANTONE.violet, PANTONE.purple, PANTONE.magenta0521],
                   [PANTONE.black, PANTONE.coolgray6, PANTONE.warmgray6]
                   ]
    
    for row, colors_row in enumerate(card_colors):
        for col, card_color in enumerate(colors_row):
            canvas2.add(SVG.taxel(PADDING_X + GRID_X * col, PADDING_Y + GRID_Y * row, card_color))
    canvas2.save()