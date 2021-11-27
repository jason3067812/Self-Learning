import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow('Tracking')

cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 0, 255, nothing)

while(True):
    frame = cv2.imread('smarties.png', 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #l_b = np.array([110, 50, 50])
    #u_b = np.array([130, 255, 255])

    LH = cv2.getTrackbarPos('LH', 'Tracking')
    LS = cv2.getTrackbarPos('LS', 'Tracking')
    LV = cv2.getTrackbarPos('LV', 'Tracking')
    UH = cv2.getTrackbarPos('UH', 'Tracking')
    US = cv2.getTrackbarPos('US', 'Tracking')
    UV = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([LH, LS, LV])
    u_b = np.array([UH, US, UV])

    mask = cv2.inRange(hsv, l_b, u_b)

    bitAnd = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('bitAnd', bitAnd)

    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()