import os
import cv2
import streamlit as st
import numpy as np
from PIL import Image
from dotenv import load_dotenv
from ultralytics import YOLO
from utils.nlp import process_command

load_dotenv()

# Load YOLO model once
model = YOLO("yolov8s.pt")

# Streamlit app
st.set_page_config(page_title="AI Computer Vision", layout="centered")
st.title("🤖 AI Computer Vision Assistant")

menu = ["Chat with Jarvis", "Object Detection"]
choice = st.sidebar.selectbox("Select Task", menu)

# ---- Chat Mode ----
if choice == "Chat with Jarvis":
    st.subheader("🧠 Ask Jarvis Anything")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("You:", key="input")

    if st.button("Send") and user_input.strip():
        reply = process_command(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Jarvis", reply))

    for sender, msg in reversed(st.session_state.chat_history):
        st.markdown(f"**{sender}**: {msg}")

# ---- Object Detection Mode ----
elif choice == "Object Detection":
    st.subheader("📷 Upload an Image")

    image_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    conf_threshold = st.slider("Confidence Threshold", 0.1, 1.0, 0.5)

    if image_file:
        img = Image.open(image_file).convert("RGB")
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Convert to array and process
        frame = np.array(img)
        results = model.predict(source=frame, conf=conf_threshold, save=False)

        if len(results[0].boxes) == 0:
            st.warning("No objects detected.")
        else:
            top = results[0].boxes[0]
            cls = int(top.cls[0])
            label = model.names[cls]
            conf = float(top.conf[0])

            st.success(f"Detected: **{label}** with confidence: {conf:.2f}")
