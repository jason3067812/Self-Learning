import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture('face_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()

    if ret==True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.8, 4) #detectMultiScale(img, scaleFactor, minNeighbors) scaleFactor:每次掃描會將圖片比例調整此參數為整張圖片pixel減少的比例。 minNeighbers:每個目標至少檢測到幾次以上，才可被認定是真數據。
    
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
            roi_gray = gray[y:y+h, x:x+w]
            roi_frame = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 3)

            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_frame, (ex,ey), (ex+ew,ey+eh), (0,255,0), 3) ####

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF==27:
            break
    else:
        break
    #time.sleep(0.04)
cap.release()
cv2.destroyAllWindows()
