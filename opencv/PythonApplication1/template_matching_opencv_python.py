import numpy as np
import cv2

img = cv2.imread('messi5.jpg', 1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi5_template.jpg', 0)
w ,h = template.shape[: : -1] #-1 代表將輸出的list排列顛倒

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED) #不斷滑動 template，得到 image 上各個位置的比較值，比較值代表相似程度(0~1)然後將 image **左上角位置，作為 result 比較值的存放位置**  #缺點 : 物體有旋轉時，會找不到 物體大小改變時，會找不到
#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

threshold = 0.95

loc = np.where(res > threshold)

for pt in zip(*loc[: : -1]): #zip(*loc[: : -1]) : loc大概長這樣 ([x1, x2, ...],[y1, y2,...]) 在zip(*loc[: : -1])後 ([y1, x1], [y2,x2], ...)
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)

#zip(*) 範例 ------------------
#a = ([1,2,3],[4,5,6],[7,8,9])
#print(a)
#for b in zip(*a):
#    print(b)
#------------------------------

#print(loc)
#print(res)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
