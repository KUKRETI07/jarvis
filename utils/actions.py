# utils/actions.py
import os
import webbrowser
import datetime
import pywhatkit
import subprocess
from voice.speak import speak

def perform_action(command):
    command = command.lower()

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "play" in command and "on youtube" in command:
        topic = command.replace("play", "").replace("on youtube", "").strip()
        speak(f"Playing {topic} on YouTube")
        pywhatkit.playonyt(topic)

    elif "search" in command:
        topic = command.replace("search", "").strip()
        speak(f"Searching {topic} on Google")
        pywhatkit.search(topic)

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open vs code" in command:
        speak("Opening Visual Studio Code")
        subprocess.Popen(["code"])

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "shutdown" in command:
        speak("Shutting down your system. Goodbye boss.")
        os.system("shutdown /s /t 1")

    else:
        return False  # No action matched

    return True
