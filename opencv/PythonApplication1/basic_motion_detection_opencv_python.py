import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    erosion = cv2.erode(thresh, None, iterations = 1)
    dilated = cv2.dilate(erosion, None, iterations = 1)
    #kernel = np.ones(3)
    #open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #cv2.drawContours(frame1, contours, -1, (0,255,0), 2) #1

    for contour in contours: #2
        (x, y, w, h) = cv2.boundingRect(contour) #用最小矩形包住輪廓取其左上右下的點

        if cv2.contourArea(contour)<400:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame1, 'Status : {}'.format('Movement'), (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    
    cv2.imshow('frame1', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()
cap.release()