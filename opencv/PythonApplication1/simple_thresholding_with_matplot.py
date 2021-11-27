import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)

_ ,th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

images = [img, th1, th2, th3, th4, th5]
titles = ['Original', 'BINARY', 'BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO', 'THRESH_TOZERO_INV']

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()