# import speech_recognition as sr
# import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 170)
#     engine.say(text)
#     engine.runAndWait()

# def listen():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print(" Listening...")
#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio)
#         print(" You said:", command)
#         return command.lower()
#     except:
#         print(" Could not understand")
#         return ""

# def process_command(command):
#     if "hello" in command:
#         return "Hello boss, how can I help you?"
#     elif "who are you" in command:
#         return "I am your personal assistant, Mini Jarvis."
#     elif "exit" in command or "bye" in command:
#         return "Goodbye boss, have a great day."
#     else:
#         return "Sorry boss, I didn’t get that yet."

# # Main loop
# speak("Jarvis is online.")
# while True:
#     command = listen()
#     if not command:
#         continue
#     response = process_command(command)
#     speak(response)
#     if "exit" in command or "bye" in command:
#         break

import os
print("API KEY:", os.getenv("OPENAI_API_KEY"))
