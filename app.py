import streamlit as st
import speech_recognition as sr
import pyttsx3
from PIL import Image
import tempfile
from utils.vision.classify import detect_object_from_camera
from utils.nlp import process_command
from utils.vision.ocr_math import  solve_math_with_easyocr


# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Voice input handler
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st.success(f"You said: **{text}**")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, could not understand the audio.")
    except sr.RequestError:
        st.error("Could not request results from Google Speech Recognition.")
    return ""

# Streamlit App
st.set_page_config(page_title="Jarvis CV App", layout="centered")
st.title(" Jarvis - Computer Vision Assistant")

choice = st.sidebar.selectbox("Select Task", [
    "Home",
    "Detect Object from Image",
    "Solve Math Equation",
    "Ask Jarvis (NLP)"
])

# ------------- Home -----------------
if choice == "Home":
    st.markdown("Welcome to **Jarvis** – Your AI Assistant with CV + NLP Power!")

# ------------- Object Detection -------------
elif choice == "Detect Object from Image":
    st.subheader("Upload an image to detect object")
    image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if image_file:
        img = Image.open(image_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            img.save(temp.name)
            label, conf = detect_object_from_camera(temp.name)
            if label:
                st.success(f"Detected: **{label}** (Confidence: {conf:.2f})")
            else:
                st.warning("No object detected.")

# ------------- Math Equation Solver ----------
elif choice == "Solve Math Equation":
    st.subheader("Upload Image of a Math Equation")
    image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if image_file:
        img = Image.open(image_file)
        st.image(img, caption="Uploaded Equation", use_column_width=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            img.save(temp.name)
            expression, result = solve_math_with_easyocr(temp.name)
            st.success(f"Equation: `{expression}`")
            st.info(f"Answer: `{result}`")

# ------------- NLP-Based Interaction ----------
elif choice == "Ask Jarvis (NLP)":
    st.subheader("Talk or Type to Jarvis")

    input_mode = st.radio("Choose input mode", ["Speak", "Type"])

    user_input = ""
    if input_mode == " Speak":
        if st.button("Start Listening"):
            user_input = recognize_speech()
    else:
        user_input = st.text_input("Type your command")

    if user_input:
        response = process_command(user_input)
        st.success(f"Jarvis: {response}")
        speak(response)
