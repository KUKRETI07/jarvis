import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings

from voice.listen import listen_command
from voice.speak import speak
from utils.nlp import process_command
from vision.eye import start_vision
from utils.actions import perform_action
from utils.vision.classify import detect_object_from_camera
from models.wake_word import listen_for_wake_word
from utils.vision.ocr_math import capture_equation_image, solve_math_with_easyocr


def main():
    listen_for_wake_word()
    speak("Hey") 

    while True:

        # Listen for actual command
        command = listen_command()
        print(command)
        if not command:
            speak("I didn't catch that.")
            continue

        # === Vision Module ===
        if "see" in command or "camera" in command or "vision" in command:
            speak("Activating vision module.")
            start_vision()
            speak("Vision module closed.")
            continue

        # === Object Detection + Explanation ===
        elif "what is this" in command or "tell me about this" in command:
            speak("Let me take a look...")
            label, confidence = detect_object_from_camera()

            if label and confidence > 0.5:
                speak(f"I see a {label}. Let me tell you more about it.")
                response = process_command(f"Tell me about a {label}")
                speak(response)
            else:
                speak("Sorry boss, I couldn't recognize that object.")
            continue

        # === Math Solver (OCR) ===
        elif "solve this" in command or "this math" in command or "equation" in command:
            image_path = capture_equation_image()
            if image_path:
             result = solve_math_with_easyocr(image_path)
            speak(result)
            continue

        if 'play' and 'youtube' in command:
            perform_action(command)

        # === Perform Action or Ask LLM ===
        if not perform_action(command):
            response = process_command(command)
            speak(response)

        # === Exit Command ===
        if "exit" in command or "bye" in command:
            speak("Shutting down, boss.")
            break


if __name__ == "__main__":
    main()

