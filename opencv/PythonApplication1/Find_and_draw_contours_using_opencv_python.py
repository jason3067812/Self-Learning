import numpy as np
import cv2

img = cv2.imread('opencv-logo.png', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY) #ret:回傳設定的門檻值
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print('Number of contours:' + str(len(contours)))

cv2.drawContours(img, contours, -1, (127, 127, 0), 6) #-1為指定所有輪廓 可以改成0,1...輪廓陣列指標繪製指定輪廓

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

