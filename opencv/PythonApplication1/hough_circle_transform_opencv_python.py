import numpy as np
import cv2

img = cv2.imread('smarties.png', 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=50)
#cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None) : dp=>累加器解析度與影象解析度的反比。dp獲取越大，累加器陣列越小。 minDist=>檢測到的圓的中心，（x,y）座標之間的最小距離。如果minDist太小，則可能導致檢測到多個相鄰的圓。如果minDist太大，則可能導致很多圓檢測不到。
#param1=>用於處理邊緣檢測(Canny higher threshold)的梯度值方法。 param2=>cv2.HOUGH_GRADIENT方法的累加器閾值。閾值越小，檢測到的圈子越多。 minRadius=>半徑的最小大小（以畫素為單位）。 maxRadius=>半徑的最大大小（以畫素為單位）。

detected = np.uint16(np.around(circles)) #np.around: 沒指定小數位數就是到整數位

#print(detected[0,1])

for (x,y,r) in detected[0,:]:
    cv2.circle(img, (x,y), r, (127,50,0), 3)
    cv2.circle(img, (x,y), 2, (0,255,255), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()