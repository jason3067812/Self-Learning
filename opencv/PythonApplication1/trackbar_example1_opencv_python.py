import numpy as np
import cv2 as cv

def blue_value(x):
    print('Blue value:'+str(x))
def green_value(x):
    print('Green value:'+str(x))
def red_value(x):
    print('Red value:'+str(x))
def switch_value(x):
    print('Switch value:'+str(x))

img = np.zeros([300, 512, 3], np.uint8)

cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, blue_value)
cv.createTrackbar('G', 'image', 0, 255, green_value)
cv.createTrackbar('R', 'image', 0, 255, red_value)
cv.createTrackbar('Switch', 'image', 0, 1, switch_value)

while(True):
    cv.imshow('image', img)

    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')

    s = cv.getTrackbarPos('Switch', 'image')

    if s==0:
        img[:]=0
    elif s==1:
        img[:] = [b,g,r]

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()