import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection   
mp_drawing = mp.solutions.drawing_utils 

img=cv2.imread("BP.jpg")
newimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
faceDetction=mp_face_detection.FaceDetection( model_selection=1, min_detection_confidence=0.5)
result=faceDetction.process(newimg)
if not result.detections:
    print("no detect")
else:

    for result in result.detections:
        mp_drawing.draw_detection(img,result)
    
cv2.imshow("result",img)
cv2.waitKey(0)
