import mediapipe as mp
import cv2


mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
# Initialize video capture
cap = cv2.VideoCapture(0)  # 0 represents the default camera, you can change it to a specific camera index if needed

# Create a face detection object
face_detection = mp_face_detection.FaceDetection()
hands = mp_hands.Hands()
while True:
    # Capture frame from the camera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Perform face detection
    face_results = face_detection.process(frame_rgb)
    
    # Perform hand detection
    hand_results = hands.process(frame_rgb)
    # Draw hand landmarks on the frame
    if face_results.detections is not None:
        for detection in face_results.detections:
            mp_drawing.draw_detection(frame, detection)

            print(detection)
    
    # Draw hand landmarks on the frame
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            print(hand_landmarks)
    # Display the resulting frame
    cv2.imshow('Hand Joint Detection', frame)
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()