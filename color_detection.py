import argparse
import cv2 as cv
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', required = True, help = 'Path to the image')
args = vars(parser.parse_args())

image = cv.imread(args['image'])
print(image.shape)
cv.imshow('image', image)

colors = pd.read_csv('colors.csv')

def get_color(r, g, b):
    min = (r - colors.iloc[0][3]) + (g - colors.iloc[0][4]) + (b - colors.iloc[0][5])
    display_color = colors.iloc[0][0]
    for i, color in colors.iterrows():
        if (min > ((r - color[3]) + (g - color[4]) + (b - color[5]))):
            min = (r - color[3]) + (g - color[4]) + (b - color[5])
            display_color = color[0]

    return display_color

def mouse_click(event, x, y,
                flags, param):

    # to check if left mouse
    # button was clicked
    if event == cv.EVENT_LBUTTONDOWN:

        # font for left click event
        font = cv.FONT_HERSHEY_TRIPLEX
        LB = 'Left Button'

        # display that left button
        # was clicked.
        r, g, b = image[x, y]
        color = get_color(r, g, b)
        cv.putText(image, color, (x, y),
                    font, 1,
                    (255, 255, 0),
                    2)
        cv.imshow('image', image)


    # to check if right mouse
    # button was clicked
    if event == cv.EVENT_RBUTTONDOWN:

        # font for right click event
        font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        RB = 'Right Button'

        # display that right button
        # was clicked.
        cv.putText(image, RB, (x, y),
                    font, 1,
                    (0, 255, 255),
                    2)
        cv.imshow('image', image)

cv.setMouseCallback('image', mouse_click)
cv.waitKey(0)
