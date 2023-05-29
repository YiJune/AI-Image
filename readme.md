# 人臉辨識
## Mediapipe
### 導入
```
import mediapipe as mp 
import cv2
```
### 讀取影像
```
cap = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection   # 建立偵測方法
mp_drawing = mp.solutions.drawing_utils           # 建立繪圖方法
```
### 開啟人臉辨識模組
```
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
# modle_selection=0 0:一個人 1:多人
```
### 是否讀取相機
```
if not cap.isOpened():
    print("Cannot open camera")
    exit()
```
### 是否讀取影像
```
 while True:
    ret, img = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
```
### 轉換色調(mediapipe為RGB)
```
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   # 將 BGR 顏色轉換成 RGB
```
### 設定人臉
```
results = face_detection.process(img2)        # 偵測人臉
```
### 畫邊界框
```
if results.detections:
    for detection in results.detections:
        mp_drawing.draw_detection(img, detection)  # 標記人臉
```
### 影像鏡像
```
img = cv2.flip(img, 1)
```
### 顯示影像設定
```
cv2.imshow('MyImg', img)
if cv2.waitKey(3) ==27: #assci code 27 :esc
    break    
