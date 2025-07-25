
             # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 

#  import cv2   # OpenCV library, used to capture video and draw on frames (for vision
#  import mediapipe as mp   #  Google's lightweight and powerful toolkit for face, hands, pose, etc.

# # def start_vision():
# #     mp_face = mp.solutions.face_detection
# #     mp_draw = mp.solutions.drawing_utils

# #     cap = cv2.VideoCapture(0) # This starts the webcam feed. 0 means default web cam 

# #     with mp_face.FaceDetection(min_detection_confidence=0.6) as face_detector: # Loads the face detection model with 60% minimum confidence.
# #         while cap.isOpened():
# #             ret, frame = cap.read()       # this is your main loop — it captures one frame at a time from the webcam.
# #             if not ret:          # frame: the actual image  , ret: a boolen value which give true if frame read the face properly 
# #                 break       # we are storing confidence so that it can “Only accept predictions above 60% confidence”

# #             # Flip and convert color  (Feels like you're looking in a mirror)
# #             frame = cv2.flip(frame, 1)     # Flips the frame horizontally (so it looks like a mirror).
# #             rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converts the image from OpenCV's default BGR format to RGB (because MediaPipe needs RGB).

# #             # Process the frame
# #             results = face_detector.process(rgb)  # results will contain any faces it finds (with coordinates and confidence).

# #             # Draw boxes so you can see what Jarvis sees. It shows that the AI has detected something.
# #             if results.detections: # if any faces are detected, draw a bounding box and confidence score using draw_detection().
# #                 for detection in results.detections:
# #                     mp_draw.draw_detection(frame, detection)

# #             cv2.imshow('Jarvis Vision - Press Q to exit', frame)

# #             if cv2.waitKey(5) & 0xFF == ord('q'):    # If you press 'q', it will break the loop and stop the vision.
# #                 break
            

# #     cap.release()           #  Properly closes the webcam and shuts down all OpenCV windows.
# #     cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp
# from voice.speak import speak

# def start_vision():
#     mp_face = mp.solutions.face_detection
#     mp_draw = mp.solutions.drawing_utils

#     speak("Activating camera. Please hold still boss.")

#     cap = cv2.VideoCapture(0)

#     num_faces = 0  # To track number of people seen
#     with mp_face.FaceDetection(min_detection_confidence=0.6) as face_detector:
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             frame = cv2.flip(frame, 1)
#             rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#             results = face_detector.process(rgb)
#             num_faces = 0  # Reset every frame

#             if results.detections:
#                 for i, detection in enumerate(results.detections):
#                     mp_draw.draw_detection(frame, detection)

#                     bboxC = detection.location_data.relative_bounding_box
#                     ih, iw, _ = frame.shape
#                     x, y = int(bboxC.xmin * iw), int(bboxC.ymin * ih)

#                     confidence = int(detection.score[0] * 100)
#                     label = f"Face {i+1}: {confidence}%"
#                     cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

#                     num_faces += 1

#             cv2.putText(frame, f"Total Faces: {num_faces}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
#             cv2.imshow('Jarvis Vision - Press Q to exit', frame)

#             if cv2.waitKey(5) & 0xFF == ord('q'):
#                 break

#     cap.release()
#     cv2.destroyAllWindows()

#     # Now speak after camera shuts down
#     if num_faces == 0:
#         speak("Boss, I could not detect anyone.")
#     elif num_faces == 1:
#         speak("Boss, I see one person in front of me.")
#     else:
#         speak(f"Boss, I see {num_faces} people in front of me.")

import cv2

def start_vision():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print(" Camera not detected.")
        return

    print("Camera activated. Press 'Q' to close.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print(" Failed to grab frame.")
            break

        cv2.imshow("JARVIS VISION MODULE", frame)

        # Wait for 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
