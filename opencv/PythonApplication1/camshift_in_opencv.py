import numpy as np
import cv2
import time

cap = cv2.VideoCapture('slow_traffic_small.mp4')
ret, frame = cap.read()
#print(frame.shape)
x, y, width, height = 300, 200, 100, 50 #自訂義
track_window = (x, y, width, height) #設定track window大小 

roi = frame[y:y+height, x:x+width] #將與track window大小相同的roi擷取
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.))) #將roi中以inRange剔除不必要資訊
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180]) ## calcHist(img, channel, mask, number of pbins, [min,Max]) #number of pbins:從最小值到最大值之間的區間(間隔)數
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX) ## 正規化 normalize(src, dst, alpha, beta, norm_type) 此處使用cv2.NORM_MINMAX故alpha為min value,beta為max value
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1) ##指定均值漂移終止一系列計算行為的方式這裡的停止條件為：均值漂移迭代10次後或者中心移動至少1個畫素時，均值漂移就停止計算中心漂移第一個標誌（EPS或CRITERIA_COUNT）表示將使用兩個條件的任意一個（計數或‘epsilon’，意味著哪個條件最先達到就停止）
#第一個標誌（EPS或CRITERIA_COUNT）表示將使用兩個條件的任意一個（計數或‘epsilon’，意味著哪個條件最先達到就停止）

cv2.imshow('roi', roi)

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1) ##反向映射(需要hist)將直方圖的值映射到目標圖上尋找圖中與直方圖統計類似的區域 cv2.calcBackProject(image, channel, hist, range, scale) 此處只映射一個channel H
        ret, track_window = cv2.CamShift(dst, track_window, term_crit) ##找尋並收斂圖中符合window大小之平均值最大的地方

        pts = cv2.boxPoints(ret) #以cv2.boxPoints找出能夠包覆ret的最小可傾斜矩形的四個頂點
        print([pts])
        pts = np.int0(pts) #int0 = int64
        final_img = cv2.polylines(frame, [pts], True, (255,0,0), 3) #折線繪圖

        cv2.imshow('dst', dst)
        cv2.imshow('final_img', final_img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
    time.sleep(0.01)
cap.release()
cv2.destroyAllWindows()
