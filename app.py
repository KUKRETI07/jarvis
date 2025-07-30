import streamlit as st
from ultralytics import YOLO
import cv2
import openai
import os
from dotenv import load_dotenv
from PIL import Image
import tempfile

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

# Load YOLO model
model = YOLO("yolov8s.pt")

# Object detection function
def detect_object_from_camera(image_path, confidence_threshold=0.5):
    frame = cv2.imread(image_path)
    results = model(frame)[0]

    if len(results.boxes) == 0:
        return "No object detected", 0.0

    top = results.boxes[0]
    cls = int(top.cls[0])
    label = model.names[cls]
    confidence = float(top.conf[0])

    if confidence < confidence_threshold:
        return "Low confidence detection", confidence

    return label, round(confidence, 2)

# NLP AI response function
def process_command(prompt):
    headers = {
        "Authorization": f"Bearer {openai.api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = openai.ChatCompletion.create(**payload)
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.set_page_config(page_title="AI CV Assistant", layout="centered")
st.title("🤖 AI Computer Vision & Assistant")

choice = st.radio("Choose a feature", ["Detect Object from Image", "Ask Jarvis (AI NLP)"])

if choice == "Detect Object from Image":
    image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    confidence = st.slider("Confidence Threshold", 0.1, 1.0, 0.5)
    
    if image_file:
        st.image(image_file, caption="Uploaded Image", use_column_width=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            img = Image.open(image_file)
            img.save(temp.name)
            label, conf = detect_object_from_camera(temp.name, confidence)
            st.success(f"Detected: **{label}** with confidence **{conf}**")

elif choice == "Ask Jarvis (AI NLP)":
    user_input = st.text_area("Type your question:")
    if st.button("Get Response"):
        if user_input.strip():
            reply = process_command(user_input)
            st.write("Jarvis:", reply)
        else:
            st.warning("Please enter a question.")
