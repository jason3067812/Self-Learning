import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorKNN () #1

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == True:
        #cv2.imshow('frame', frame)

        fgmask = fgbg.apply(frame) ###
        cv2.imshow('fgmask', fgmask)
    else:
        break

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

"""
BackgroundSubtractorMOG
這是一種以高斯混合（Gaussian Mixture-base）為基礎的前景/背景分離技術，由P. KadewTraKuPong和R. Bowden於2001年發表的論文「An improved adaptive background mixture model for real-time tracking with shadow detection」發展而來。它利用一種指定K值（K=3~5）的高斯分佈來計算背景像素。

指令：cv2.bgsegm.createBackgroundSubtractorMOG()

參數：int history=200, int nmixtures=5, double backgroundRatio=0.7, double noiseSigma=0

BackgroundSubtractorMOG2
BackgroundSubtractorMOG的改良版，依據Z.Zivkovic,的兩篇論文：2004年「Improved adaptive Gausian mixture model for background subtraction」以及2006年「Efficient Adaptive Density Estimation per Image Pixel for the Task of Background Subtraction」發展而來。理論上，MOG2比起MOG有更好的光照差異處理，此外，MOG2支援multi-threads，因此速度快近一倍。

指令：cv2.createBackgroundSubtractorMOG2()

參數：int history=500, double varThreshold=16, bool detectShadows=true

BackgroundSubtractorGMG
此技術合併了固定的背景圖像預測（statistical background image estimation）以及像素貝葉氏分割（per-pixel Bayesian segmentation）理論，是來自於三位學者（Andrew B. Godbehere, Akihiro Matsukawa, Ken Goldberg）於2012年的paper： Visual Tracking of Human Visitors under Variable-Lighting Conditions for a Responsive Audio Art Installation。

指令：cv2.bgsegm.createBackgroundSubtractorGMG ()

參數：int initializationFrames=120, double decisionThreshold=0.8

BackgroundSubtractorKNN
K近鄰（K-nearest neigbours）為基礎的前景/背景分離技術，來自於由Zoran Zivkovic 和Ferdinand van der Heijden的論文「Efficient adaptive density estimation per image pixel for the task of background subtraction.」

指令：cv2.createBackgroundSubtractorKNN ()

參數：int history=500, double dist2Threshold=400.0, bool detectShadows=True
"""