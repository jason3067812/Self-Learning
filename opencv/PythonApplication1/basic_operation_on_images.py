import numpy as np
import cv2

img1 = cv2.imread('messi5.jpg', 1)
img2 = cv2.imread('opencv-logo.png', 1)

#圖片資訊
print(img1.shape)
print(img1.size)
print(img1.dtype)

#channel分割 融合
b,g,r = cv2.split(img1)
img = cv2.merge((b,g,r))

#cv2.imshow('img', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#影像覆蓋
ball = img1[280:340, 330:390]
img1[273:333, 100:160] = ball

#cv2.imshow('img', img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#影像相加(shape需相同)
img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

#dst = cv2.add(img1, img2)
dst = cv2.addWeighted(img1, .5, img2, .2, 0) #權重模式相加

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()