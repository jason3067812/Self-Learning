
import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

cv.namedWindow('image')

cv.createTrackbar('CP', 'image', 0, 400, nothing)
cv.createTrackbar('Color/Gray', 'image', 0, 1, nothing)

while(True):
    img = cv.imread('lena.jpg', 1)

    pos = cv.getTrackbarPos('CP', 'image')
    s = cv.getTrackbarPos('Color/Gray', 'image')

    font = cv.FONT_HERSHEY_COMPLEX
    img = cv.putText(img, str(pos), (10,400), font, 4, (0,0,255), 7, cv.LINE_AA)

    if s==0:
        pass
    elif s==1:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    cv.imshow('image', img)
cv.destroyAllWindows()