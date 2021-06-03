import cv2 as cv
import numpy as np

character_dictionary = dict()
all_letters = "abcdefghijklmnopqrstuvwxyz"

window_name = 'Image'

font = cv.FONT_HERSHEY_TRIPLEX
fontScale = 10
color = (0, 0, 0)
thickness = 15

char_canvas = np.ones((400, 400, 3), np.uint8) * 255
script_canvas = np.ones((400, 250, 3), np.uint8) * 255
white_canvas = char_canvas.copy()

# generate normal lowercase character images
for char in all_letters:
    white_canvas = char_canvas.copy()
    # get boundary of this text
    textsize = cv.getTextSize(char, font, fontScale, thickness)[0]
    white_canvas = np.ones((400, textsize[0] + 50, 3), np.uint8) * 255
    # get coords based on boundary
    textX = int((white_canvas.shape[1] - textsize[0]) / 2)
    textY = int((white_canvas.shape[0] + textsize[1]) / 2)
    org = (textX, textY)

    char_file = cv.putText(white_canvas, char, org, font,
                fontScale, color, thickness, cv.LINE_AA)
    cv.imwrite(char + ".png", white_canvas)

    # cv.imshow(window_name, char_file)

    cv.waitKey(0)

# generate normal uppercase character images
for char in all_letters:
    char = char.upper()
    white_canvas = char_canvas.copy()
    # get boundary of this text
    textsize = cv.getTextSize(char, font, fontScale, thickness)[0]
    white_canvas = np.ones((400, textsize[0] + 50, 3), np.uint8) * 255
    # get coords based on boundary
    textX = int((white_canvas.shape[1] - textsize[0]) / 2)
    textY = int((white_canvas.shape[0] + textsize[1]) / 2)
    org = (textX, textY)

    char_file = cv.putText(white_canvas, char, org, font,
                fontScale, color, thickness, cv.LINE_AA)
    cv.imwrite(char.lower() + "_upper" + ".png", white_canvas)

    # cv.imshow(window_name, char_file)

    cv.waitKey(0)

# generate superscript character images
for char in all_letters:
    white_canvas = script_canvas.copy()
    # get boundary of this text
    textsize = cv.getTextSize(char, font, fontScale - 5, thickness - 7)[0]

    # get coords based on boundary
    textX = int((white_canvas.shape[1] - textsize[0]) / 2)
    textY = int(textsize[1])
    org = (textX, textY)

    char_file = cv.putText(white_canvas, char, org, font,
                fontScale - 5, color, thickness - 7, cv.LINE_AA)
    cv.imwrite(char + "_superscript" + ".png", white_canvas)

    # cv.imshow(window_name, char_file)

    cv.waitKey(0)

# generate subscript character images
for char in all_letters:
    white_canvas = script_canvas.copy()
    # get boundary of this text
    textsize = cv.getTextSize(char, font, fontScale - 5, thickness - 7)[0]

    # get coords based on boundary
    textX = int((white_canvas.shape[1] - textsize[0]) / 2)
    textY = int((white_canvas.shape[0] - (textsize[1] / 2)))
    org = (textX, textY)

    char_file = cv.putText(white_canvas, char, org, font,
                fontScale - 5, color, thickness - 7, cv.LINE_AA)
    cv.imwrite(char + "_subscript" + ".png", white_canvas)

    # cv.imshow(window_name, char_file)

    cv.waitKey(0)
