
        # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 
  

# import cv2   # For camera access and image processing (OpenCV)
# import numpy as np  # For handling pixel arrays
# from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
# from tensorflow.keras.preprocessing import image
# from voice.speak import speak

# # Load pre-trained model
# # model = MobileNetV2(weights='imagenet')  # pre-trained image classification model

# # def capture_frame():
# #     cap = cv2.VideoCapture(0)          # Open the webcam (device 0)
# #     ret, frame = cap.read()            # Read a frame
# #     cap.release()                      # Release the camera
# #     if not ret:
# #         return None                    # If failed, return None
# #     return frame                       # Return the image frame

# def capture_frame():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Cannot open camera")
#         return None

#     print("Opening camera window...")
#     speak("Please show me the object.")

#     for _ in range(30):  # Warm-up and show feed for 30 frames (~1 second)
#         ret, frame = cap.read()
#         if not ret:
#             continue

        

#         # Show the live frame
#         cv2.imshow('Jarvis Camera - Show Object', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Capture the final frame
#     ret, frame = cap.read()
#     cap.release()
#     cv2.destroyAllWindows()

#     if not ret:
#         return None
#     return frame

# def classify_frame(frame):
#     img = cv2.resize(frame, (224, 224))                    # Resize for model input
#     img_array = image.img_to_array(img)                    # Convert image to array
#     img_array = np.expand_dims(img_array, axis=0)          # Add batch dimension
#     img_array = preprocess_input(img_array)                # Preprocess for MobileNetV2

#     predictions = model.predict(img_array)                 # Run prediction
#     decoded = decode_predictions(predictions, top=1)[0][0] # Decode top-1 result
#     label = decoded[1]                                     # Get class name
#     confidence = decoded[2]                                # Get confidence score
#     return label, confidence

# def detect_object_from_camera():
#     frame = capture_frame()
#     if frame is None:
#         return None, 0.0  #  to avoid UnboundLocalError
#     label, confidence = classify_frame(frame)
#     return label, confidence

# decode_predictions Converts raw model outputs to readable labels
# note:  preprocess_input Prepares image to fit MobileNet’s format


from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

def detect_object_from_camera(image_path=None, confidence_threshold=0.5):
    if image_path:
        frame = cv2.imread(image_path)
    else:
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            return None, 0.0
        ret, frame = cam.read()
        cam.release()

    results = model(frame)[0]
    if len(results.boxes) == 0:
        return None, 0.0

    top = results.boxes[0]
    cls = int(top.cls[0])
    label = model.names[cls]
    confidence = float(top.conf[0])  

    if float(confidence) < float(confidence_threshold):  
        return None, confidence
    return label, confidence

 