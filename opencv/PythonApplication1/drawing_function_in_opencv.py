import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 10)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), 10)

img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 5) #thickness=-1 fill hole
img = cv2.circle(img, (447,64), 64, (0,128,128), 8)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCV', (10,400), font, 4, (255,255,255), 7, cv2.LINE_AA)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
