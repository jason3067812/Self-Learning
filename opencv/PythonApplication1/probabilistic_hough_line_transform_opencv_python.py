import numpy as np
import cv2

#img = cv2.imread('sudoku.png', 1) #1
img = cv2.imread('road.jpg', 1) #2
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100,minLineLength=100, maxLineGap=8)
#cv2.HoughLinesP(image, rho, theta, threshold, minLineLength, maxLineGap) : maxLineGap=>maximum allowed gapbetween line segments to treat them as single line

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow('Canny', edges)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
