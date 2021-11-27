import numpy as np
import cv2

img = cv2.imread('chessboard.png', 1)

cv2.imshow('chessboard', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray) #計算intensity一定會有小數點
dst = cv2.cornerHarris(gray, 2, 3, 0.04) #cornerHarris(img, blockSize, ksize, k) blockSize:檢測中要考慮的領域大小。 ksize:soble kernel size。 k:檢測中計算常數。
dst = cv2.dilate(dst, None)

img[dst > 0.01*dst.max()] = (0,0,255) #0.01*dst.max()為通常決定是否圍角點的閥值 [0.01可改]

cv2.imshow('dst', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

