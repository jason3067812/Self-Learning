import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT'in i]
#print(events)

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = 'Position:' + str(x) + ',' + str(y)
        
        cv2.putText(img, strXY, (x,y), font, .5, (255,255,0), 1, cv2.LINE_AA)
        cv2.circle(img, (x,y), 1, (255,255,0), -1)
        cv2.imshow('img', img)
    if event == cv2.EVENT_FLAG_RBUTTON:
        font = cv2.FONT_HERSHEY_COMPLEX
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strCOLOR = 'Color:' + str(blue) + ',' + str(green) + ',' + str(red)
        
        cv2.putText(img, strCOLOR, (x,y), font, .5, (0,255,255), 1, cv2.LINE_AA)
        cv2.circle(img, (x,y), 1, (0,255,255), -1)
        cv2.imshow('img', img)

img = cv2.imread('lena.jpg', 1)
#img = np.zeros([512,512,3], np.uint8)
cv2.imshow('img', img)

cv2.setMouseCallback('img', click_event) #****

cv2.waitKey(0)
cv2.destroyAllWindows()