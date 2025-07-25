import gradio as gr
from utils.vision.classify import detect_object_from_camera
from utils.nlp import process_command

chat_interface = gr.Interface(
    fn=process_command,
    inputs=gr.Textbox(lines=2, placeholder="Ask jarvis anything..."),
    outputs="text",
    title="jarvis AI - Chat",
    description=" Intelligent Assistant. Solves math too!"
) 

object_interface = gr.Interface(
    fn=detect_object_from_camera,
    inputs=gr.Image(type="pil"),
    outputs="image",
    title="Object Detector",
    description="Upload an image and jarvis will detect objects in it."
)

demo = gr.TabbedInterface(
    interface_list=[chat_interface, object_interface],
    tab_names=["💬 Chat & Math", "📷 Object Detection"]
)

demo.launch(share=True)
