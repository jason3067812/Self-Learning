import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT'in i]
#print(events)

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)

        mycolorImage = np.zeros([512, 512, 3], np.uint8)

        mycolorImage[:] = [blue, green, red]

        cv2.imshow('color', mycolorImage)

img = cv2.imread('lena.jpg', 1)
#img = np.zeros([512,512,3], np.uint8)
cv2.imshow('img', img)
cv2.setMouseCallback('img', click_event) #****

cv2.waitKey(0)
cv2.destroyAllWindows()