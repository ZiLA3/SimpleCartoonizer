import cv2 as cv
import numpy as np

def cartoonize(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    gray = cv.GaussianBlur(gray, (5, 5), 0)

    edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)
    edges = cv.erode(edges, cv.getStructuringElement(cv.MORPH_RECT, (3, 3)))

    color = cv.bilateralFilter(img, 9, 250, 21250)
    cartoon = cv.bitwise_and(color, color, mask=edges)

    return cartoon

def show(img, title='Image'):
    cartoon = cartoonize(img)
    merge = np.hstack((img, cartoon))
    cv.imshow(title, merge)

img1 = cv.imread('Images/Castle.png')
img2 = cv.imread('Images/Cat.png')

show(img1, 'Good Image')
show(img2, 'Bad Image')

cv.waitKey(0)