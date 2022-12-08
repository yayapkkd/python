# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:19:03 2022

@author: YAYA
"""

import cv2
import mediapipe as mp     # 載入 mediapipe 函式庫
from sys import exit       # import exit

mp_drawing = mp.solutions.drawing_utils         # mediapipe 繪圖方法
mp_drawing_styles = mp.solutions.drawing_styles # mediapipe 繪圖樣式
mp_holistic = mp.solutions.holistic             # mediapipe 全身偵測方法

cap = cv2.VideoCapture(0)  # 視頻截取


with mp_holistic.Holistic(                      # mediapipe 啟用偵測全身
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as holistic:

    if not cap.isOpened():                      # 若偵測不到相機
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()                   # 讀取照片
        if not ret:                             # 若收不到幀
            print("Cannot receive frame")
            break
        img = cv2.resize(img,(520,300))
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 轉換成 RGB
        results = holistic.process(img2)              # 開始偵測全身
        # 面部偵測，繪製臉部網格
        mp_drawing.draw_landmarks(
            img,
            results.face_landmarks,
            mp_holistic.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_contours_style())
        # 身體偵測，繪製身體骨架
        mp_drawing.draw_landmarks(
            img,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles
            .get_default_pose_landmarks_style())

        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()    #關閉所有視窗