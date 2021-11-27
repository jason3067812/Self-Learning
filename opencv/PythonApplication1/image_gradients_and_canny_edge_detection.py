import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0) #1
#img = cv2.imread('sudoku.png', 0) #2

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #cv2.CV_64F:一種資料型態類似float64 因為計算gradient會有負數 所以資料型態需為浮點數
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelcombined = cv2.bitwise_or(sobelX, sobelY)

edges = cv2.Canny(img, 100, 200)

images = [img, lap, sobelX, sobelY, sobelcombined, edges]
titles = ['img', 'Laplacian', 'sobelX', 'sobelY', 'sobelcombined', 'Canny']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
