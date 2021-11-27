import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)

kernel = np.ones([5,5], np.uint8)

dilate = cv2.dilate(mask, kernel, iterations=2) #iterations重複做幾次
erosion = cv2.erode(mask, kernel, iterations=2)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel, iterations=1)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel, iterations=1)

images = [img, mask, dilate, erosion, opening, closing, mg, th]
titles = ['img', 'mask', 'dilate', 'erosion', 'opening', 'closing', 'gradient', 'tophat']

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

#腐蝕	erode	erosion = cv2.erode(src=girl_pic, kernel=kernel)	在窗中，只要含有０，則窗內全變為０，可以去淺色噪點	淺色成分被腐蝕
#膨脹	dilate	dilation = cv2.dilate(src=girl_pic, kernel=kernel)	在窗中，只要含有１，則窗內全變為１，可以增加淺色成分	淺色成分得膨脹
#開運算	morphology-open	opening = cv2.morphologyEx(girl_pic, cv2.MORPH_OPEN, kernel)	先腐蝕，後膨脹，去白噪點	先合再開，對淺色成分不利
#閉運算	morphology-close	closing = cv2.morphologyEx(girl_pic, cv2.MORPH_CLOSE, kernel)	先膨脹，後腐蝕，去黑噪點	先開再合，淺色成分得勢
#形態學梯度	morphology-grandient	gradient = cv2.morphologyEx(girl_pic, cv2.MORPH_GRADIENT, kernel)	一幅影象腐蝕與膨脹的區別，可以得到輪廓	數值上解釋為：膨脹減去腐蝕
#禮帽	tophat	tophat = cv2.morphologyEx(girl_pic, cv2.MORPH_TOPHAT, kernel)	原影象減去開運算的差	數值上解釋為：原影象減去開運算
#黑帽	blackhat	blackhat = cv2.morphologyEx(girl_pic, cv2.MORPH_BLACKHAT, kernel)	閉運算減去原影象的差	數值上解釋為：閉運算減去原影象