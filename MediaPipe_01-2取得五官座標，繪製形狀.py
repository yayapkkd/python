from sys import exit       # import exit
import cv2
import mediapipe as mp     # 載入 mediapipe 函式庫

cap = cv2.VideoCapture(0)  # 視頻截取
mp_face_detection = mp.solutions.face_detection   # 建立偵測方法
mp_drawing = mp.solutions.drawing_utils           # 建立繪圖方法

with mp_face_detection.FaceDetection(             # 開始偵測人臉
    model_selection=0, min_detection_confidence=0.5) as face_detection:

    if not cap.isOpened():                        # 若偵測不到相機
        print("Cannot open camera")
        exit()
    while True:
        ret, img = cap.read()                     # 讀取照片
        if not ret:                               # 若收不到幀
            print("Cannot receive frame")
            break
        size = img.shape   # 取得攝影機影像尺寸
        w = size[1]        # 取得畫面寬度
        h = size[0]        # 取得畫面高度
        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 顏色轉換成 RGB
        results = face_detection.process(img2)        # 偵測人臉

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(img, detection)  # 標記人臉
                s = detection.location_data.relative_bounding_box     # 取得人臉尺寸
                eye = int(s.width*w*0.1)                              # 計算眼睛大小 ( 人臉尺寸*0.1 )
                a = detection.location_data.relative_keypoints[0]     # 取得左眼座標
                b = detection.location_data.relative_keypoints[1]     # 取得右眼座標
                ax, ay = int(a.x*w), int(a.y*h)                       # 計算左眼真正的座標
                bx, by = int(b.x*w), int(b.y*h)                       # 計算右眼真正的座標
                cv2.circle(img,(ax,ay),(eye+10),(255,255,255),-1)     # 畫左眼白色大圓 ( 白眼球 )
                cv2.circle(img,(bx,by),(eye+10),(255,255,255),-1)     # 畫右眼白色大圓 ( 白眼球 )
                cv2.circle(img,(ax,ay),eye,(0,0,0),-1)                # 畫左眼黑色大圓 ( 黑眼球 )
                cv2.circle(img,(bx,by),eye,(0,0,0),-1)                # 畫右眼黑色大圓 ( 黑眼球 )
                cv2.circle(img,(ax-8,ay-8),(eye-15),(255,255,255),-1) # 畫左眼白色小圓 ( 反光 )
                cv2.circle(img,(bx-8,by-8),(eye-15),(255,255,255),-1) # 畫右眼白色小圓 ( 反光 )
               
        cv2.imshow('oxxostudio', img)
        if cv2.waitKey(5) == ord('q'):
            break    # 按下 q 鍵停止
cap.release()
cv2.destroyAllWindows()    #關閉所有視窗
