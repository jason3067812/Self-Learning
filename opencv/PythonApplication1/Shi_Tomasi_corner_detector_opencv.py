import numpy as np
import cv2

img = cv2.imread('pic1.png', 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) #Harris corner效能較慢 goodFeaturesToTrack是其進階版本且支援Shi Tomasi corner算法
#goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
#maxCorners:Maximum number of corners to return. If there are more corners than are found, the strongest of them is returned.
#qualityLevel:Parameter characterizing the minimal accepted quality of image corners. The parameter value is multiplied by the best corner quality measure, which is the minimal eigenvalue (see cornerMinEigenVal() ) or the Harris function response (see cornerHarris() ). The corners with the quality measure less than the product are rejected. For example, if the best corner has the quality measure = 1500, and the qualityLevel=0.01 , then all the corners with the quality measure less than 15 are rejected.
#minDistance:Minimum possible Euclidean distance between the returned corners.

corners = np.int0(corners) #為了能畫在圖上須將座標轉為正整數

for i in corners:
    x,y = i.ravel() #展平為1D array
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

