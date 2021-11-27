import numpy as np
import cv2

img = cv2.imread('shapes.jpg', 1)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img_gray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:

    if cv2.arcLength(contour, True)<50 or cv2.arcLength(contour, True)>2000: #面積太大或太小的封閉輪廓剔除
        continue

    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True) #cv2.approxPolyDP:自動決定輪廓中的點是否被保留以周長值的1%~5%做為參考
    cv2.drawContours(img, [approx], 0, (0,0,0), 2) #approx:是一個numap array 需要將其轉換為list才能讓cv2.drawContours吃進來

    x = approx.ravel()[0] #將整個list展平成1D array後取第一個指標的值 [亦可用flatten()]
    y = approx.ravel()[1]-5 #將整個list展平成1D array後取第二個指標的值

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img, 'Square', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else:
            cv2.putText(img, 'Rectangle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    elif len(approx) == 10:
        cv2.putText(img, 'Star', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    else:
        cv2.putText(img, 'Circle', (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
    
#print(type([approx]))
#print(type(approx))
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
