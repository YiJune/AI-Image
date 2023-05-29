import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection   
mp_drawing = mp.solutions.drawing_utils 

img=cv2.imread("BP.jpg")
newimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
faceDetction=mp_face_detection.FaceDetection( model_selection=1, min_detection_confidence=0.5)
result=faceDetction.process(newimg)
if  result.detections:
      for detection in result.detections:
        bbox = detection.location_data.relative_bounding_box
        ih, iw, _ = img.shape
        xmin = int(bbox.xmin * iw)
        ymin = int(bbox.ymin * ih)
        w = int(bbox.width * iw)
        h = int(bbox.height * ih)

        
        face_img = img[ymin:ymin + h, xmin:xmin + w]
        mosaic_face = cv2.resize(face_img, (8, 8), interpolation=cv2.INTER_NEAREST)
        mosaic_face = cv2.resize(mosaic_face, (w, h), interpolation=cv2.INTER_NEAREST)
        img[ymin:ymin + h, xmin:xmin + w] = mosaic_face


        

    
    
img = cv2.resize(img, (w,h)) 
cv2.imshow("result",img)
cv2.waitKey(0)
