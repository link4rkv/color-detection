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
        diff = abs(r - int(color[3])) + abs(g - int(color[4]))+ abs(b - int(color[5]))
        if (min > diff):
            min = diff
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
        r = int(r)
        g = int(g)
        b = int(b)
        cv.rectangle(image,(20,20), (750,60), (b,g,r), -1)
        cv.putText(image, color, (50, 50),
                    font, 1,
                    (0, 0, 0),
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
