import cv2

img = cv2.imread("lena.jpg",1) #1:color 0:gray -1:add apha axis

cv2.imshow("lena",img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite("lena_copy.jpg",img)
	cv2.destroyAllWindows()
