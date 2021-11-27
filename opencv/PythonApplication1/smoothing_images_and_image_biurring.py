import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('eye.jpg', 0) #1
#img = cv2.imread('water.png', 0) #2
img = cv2.imread('lena.jpg', 1) #3
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #3

kernel = np.ones([5,5], np.float32)/25
dst = cv2.filter2D(img, -1, kernel) #ddepth=-1 輸出和原有圖像相同深度之圖像
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)#color σ=0 越遠的像素給予的補正權重 #適合清除高頻雜訊
median = cv2.medianBlur(img, 5) #適合清除salt and pepper noise
bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75) #(src, d, sigmaColor, sigmaSpace) d:kernel diameter. sigmaColor:空間高斯函數標準差. sigmaSpace:灰度值相似性高斯函數標準差. 通常sigmaColor=sigmaSpace<150 #similar to median filter and enhense edge

images = [img, dst, blur, gblur, median]
titles = ['img', 'dst', 'blur', 'gblur', 'median']

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.xticks([])

plt.show()