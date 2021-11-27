import numpy as np
import cv2

apple = cv2.imread('apple.jpg', 1)
orange = cv2.imread('orange.jpg', 1)

print(apple.shape)
print(orange.shape)
apple_orange = np.hstack((apple[:, :256], orange[:, 256:])) #沿水平方向疊起來 #示範不模糊直接疊起來的結果

#Apple Gaussian Pyramid
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy) #縮小1/4倍
    gp_apple.append(apple_copy)

#Orange Gaussian Pyramid
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy) #縮小1/4倍
    gp_orange.append(orange_copy)

#Generate Laplacian Pyramid for apple
apple_copy = gp_apple[5] ###
apple_lp = [apple_copy]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i]) #放大4倍
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    apple_lp.append(laplacian)

#Generate Laplacian Pyramid for orange
orange_copy = gp_orange[5] ###
orange_lp = [orange_copy]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i]) #放大4倍
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    orange_lp.append(laplacian)

#Add left and right halves of images in each level
apple_orange_pyramid = []
n = 0

for lap_apple, lap_orange in zip(apple_lp, orange_lp):
    n+=1
    cols, rows, ch = lap_apple.shape
    laplacian = np.hstack((lap_apple[:, :int(cols/2)], lap_orange[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    #cv2.imshow(str(n), laplacian) #第一張是彩圖

#reconstruct image
apple_orange_reconstruct = apple_orange_pyramid[0] ###

for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct) #放大4倍失去細節
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct) #在每次放大後加回細節

cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()
