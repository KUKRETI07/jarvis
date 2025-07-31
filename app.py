# # import streamlit as st
# # import speech_recognition as sr
# # import pyttsx3
# # from PIL import Image
# # import tempfile
# # from utils.vision.classify import detect_object_from_camera
# # from utils.nlp import process_command
# # from utils.vision.ocr_math import  solve_math_with_easyocr


# # # Initialize text-to-speech engine
# # engine = pyttsx3.init()
# # engine.setProperty("rate", 150)

# # # Speak text
# # def speak(text):
# #     engine.say(text)
# #     engine.runAndWait()

# # # Voice input handler
# # def recognize_speech():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         st.info("Listening...")
# #         audio = r.listen(source)
# #     try:
# #         text = r.recognize_google(audio)
# #         st.success(f"You said: **{text}**")
# #         return text
# #     except sr.UnknownValueError:
# #         st.error("Sorry, could not understand the audio.")
# #     except sr.RequestError:
# #         st.error("Could not request results from Google Speech Recognition.")
# #     return ""

# # # Streamlit App
# # st.set_page_config(page_title="Jarvis CV App", layout="centered")
# # st.title(" Jarvis - Computer Vision Assistant")

# # choice = st.sidebar.selectbox("Select Task", [
# #     "Home",
# #     "Detect Object from Image",
# #     "Solve Math Equation",
# #     "Ask Jarvis (NLP)"
# # ])

# # # ------------- Home -----------------
# # if choice == "Home":
# #     st.markdown("Welcome to **Jarvis** – Your AI Assistant with CV + NLP Power!")

# # # ------------- Object Detection -------------
# # elif choice == "Detect Object from Image":
# #     st.subheader("Upload an image to detect object")
# #     image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
# #     if image_file:
# #         img = Image.open(image_file)
# #         st.image(img, caption="Uploaded Image", use_column_width=True)
# #         with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
# #             img.save(temp.name)
# #             label, conf = detect_object_from_camera(temp.name)
# #             if label:
# #                 st.success(f"Detected: **{label}** (Confidence: {conf:.2f})")
# #             else:
# #                 st.warning("No object detected.")

# # # ------------- Math Equation Solver ----------
# # elif choice == "Solve Math Equation":
# #     st.subheader("Upload Image of a Math Equation")
# #     image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
# #     if image_file:
# #         img = Image.open(image_file)
# #         st.image(img, caption="Uploaded Equation", use_column_width=True)
# #         with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
# #             img.save(temp.name)
# #             expression, result = solve_math_with_easyocr(temp.name)
# #             st.success(f"Equation: `{expression}`")
# #             st.info(f"Answer: `{result}`")

# # # ------------- NLP-Based Interaction ----------
# # elif choice == "Ask Jarvis (NLP)":
# #     st.subheader("Talk or Type to Jarvis")

# #     input_mode = st.radio("Choose input mode", ["Speak", "Type"])

# #     user_input = ""
# #     if input_mode == " Speak":
# #         if st.button("Start Listening"):
# #             user_input = recognize_speech()
# #     else:
# #         user_input = st.text_input("Type your command")

# #     if user_input:
# #         response = process_command(user_input)
# #         st.success(f"Jarvis: {response}")
# #         speak(response)


# # from flask import Flask, render_template, request
# # import os
# # import openai
# # from utils.math_solver import solve_math
# # from utils.object_detection import detect_objects
# # from werkzeug.utils import secure_filename

# # app = Flask(__name__)
# # app.config["UPLOAD_FOLDER"] = "static/uploads"

# # # Load your OpenAI key
# # openai.api_key = os.getenv("OPENAI_API_KEY")

# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #     response = ""
# #     object_result = ""
# #     math_result = ""
    
# #     if request.method == "POST":
# #         user_input = request.form.get("prompt")
# #         task = request.form.get("task")

# #         # Task: Chat
# #         if task == "chat":
# #             completion = openai.ChatCompletion.create(
# #                 model="gpt-3.5-turbo",
# #                 messages=[{"role": "user", "content": user_input}]
# #             )
# #             response = completion["choices"][0]["message"]["content"]

# #         # Task: Math Solver
# #         elif task == "math":
# #             math_result = solve_math(user_input)

# #         # Task: Object Detection
# #         elif task == "object":
# #             file = request.files["image"]
# #             if file:
# #                 filename = secure_filename(file.filename)
# #                 filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
# #                 file.save(filepath)
# #                 object_result = detect_objects(filepath)
    
# #     return render_template("index.html", response=response, math_result=math_result, object_result=object_result)

# # if __name__ == "__main__":
# #     app.run(debug=True)


# # app.py
# import gradio as gr
# from utils.vision.classify import detect_object_from_camera
# from utils.nlp import process_command

# chat_interface = gr.Interface(
#     fn=process_command,
#     inputs=gr.Textbox(lines=2, placeholder="Ask jarvis anything..."),
#     outputs="text",
#     title="jarvis AI - Chat",
#     description=" Intelligent Assistant. Solves math too!"
# ) 

# object_interface = gr.Interface(
#     fn=detect_object_from_camera,
#     inputs=gr.Image(type="pil"),
#     outputs="image",
#     title="Object Detector",
#     description="Upload an image and jarvis will detect objects in it."
# )

# demo = gr.TabbedInterface(
#     interface_list=[chat_interface, object_interface],
#     tab_names=["💬 Chat & Math", "📷 Object Detection"]
# )

# demo.launch(share=True)



import os
import cv2
import gradio as gr
from dotenv import load_dotenv
from ultralytics import YOLO
from functools import lru_cache
from utils.nlp import process_command  # Make sure this imports from the updated cohere-based nlp.py

# Load environment variables
load_dotenv()

# Cache the YOLO model to avoid reloading every time
@lru_cache()
def load_yolo_model():
    return YOLO("yolov8s.pt")

# Chatbot function using cohere
def chat_with_jarvis(message, history):
    history = history or []
    reply = process_command(message)
    history.append((message, reply))
    return history, history

# Object Detection
def detect_objects(image_path=None, confidence_threshold=0.5):
    if image_path is None:
        return "Please upload an image", 0.0

    frame = cv2.imread(image_path)
    model = load_yolo_model()
    results = model.predict(source=frame, conf=confidence_threshold, save=False)

    max_conf = 0
    label = "No object detected"
    for r in results:
        for box in r.boxes:
            conf = float(box.conf)
            if conf > max_conf:
                max_conf = conf
                label = model.names[int(box.cls)]

    return label, round(max_conf, 2)

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Computer Vision Assistant (Chat + Object Detection)")

    with gr.Tab("💬 Chat with Jarvis"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="Ask something like 'What is AI?'...")
        clear = gr.Button("Clear Chat")

        msg.submit(chat_with_jarvis, [msg, chatbot], [chatbot, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    with gr.Tab("🎯 Object Detection"):
        image_input = gr.Image(type="filepath", label="Upload an image")
        confidence_slider = gr.Slider(0.1, 1.0, value=0.5, label="Confidence Threshold")
        detect_button = gr.Button("Detect")

        label_output = gr.Textbox(label="Detected Object")
        confidence_output = gr.Number(label="Confidence Score")

        detect_button.click(
            detect_objects,
            inputs=[image_input, confidence_slider],
            outputs=[label_output, confidence_output]
        )

demo.launch()
