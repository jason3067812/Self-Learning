import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#------------------1---------------------#
#cv2.imshow('img_gray', img_gray)

#plt.hist(img_gray.ravel(), 256, [0,256])
#plt.show()
#----------------------------------------#

#------------------2---------------------#
#b, g, r = cv2.split(img)
#cv2.imshow('b', b)
#cv2.imshow('g', g)
#cv2.imshow('r', r)

#plt.hist(b.ravel(), 256, [0,256], color=(0,0,1,1)) #RGBA float[0~1] A:alpha 透明度
#plt.hist(g.ravel(), 256, [0,256], color=(0,1,0,1))
#plt.hist(r.ravel(), 256, [0,256], color=(1,0,0,1))
#plt.show()
#----------------------------------------#

#------------------3---------------------#
hist = cv2.calcHist([img_gray], [0], None, [256], [0,256]) #channel = [0] 代表看 channel軸的第一軸 若彩圖則有三個軸
plt.plot(hist)

plt.show()
#----------------------------------------#

cv2.waitKey(0)
cv2.destroyAllWindows()