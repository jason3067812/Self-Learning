import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)
layer = img.copy()

gp=[layer]

for i in range(6): #Gaussian pyramid
    layer = cv2.pyrDown(layer) #縮小1/4倍 #損失細節資訊
    gp.append(layer)
    #cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)

#A level in Laplcian Pyramid is formed bythe difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid (縮小後的圖放大上去後用原圖減去即為 Laplacian Pyramid 即為縮小後失去的細節)
lp = [layer]

for i in range(5, 0, -1): #Laplacian Pyramid
    #5~1
    gaussian_extended = cv2.pyrUp(gp[i]) #放大4倍
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    lp.append(laplacian)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

