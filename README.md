# Jarvis-CV: A Voice-Controlled Personal Assistant with Vision 🌐🎙️👁️

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT-blue)
![SpeechRecognition](https://img.shields.io/badge/Voice-Controlled-success)
![ComputerVision](https://img.shields.io/badge/Computer-Vision-purple)

---

## 🚀 Project Overview

**Jarvis-CV** is an intelligent computer vision, voice-based personal assistant that responds to your spoken queries and detect object from the camera and tell you about that object , you can operate it from you command and it will work like real jarvis (you saw in marvel movies) . Powered by **NLP**, **TTS**, **speech recognition**, and **computer vision**

You can ask it anything—from your current location, weather, or time—to performing tasks like opening a website, searching Wikipedia, or identifying objects using your webcam.

> This is a prototype that showcases how NLP + CV + TTS + Voice recognition can be combined into a **simple yet powerful AI assistant**.

---

## 🎯 Features

- 🔊 Voice-controlled input (no keyboard needed!)
- 🤖 NLP-powered conversation with OpenAI
- 🎤 Text-to-speech response
- 🌐 Internet search and Wikipedia summarization
- 📸 Real-time object detection with computer vision (OpenCV)
- 📁 Clean and minimal Streamlit web UI

---

## 🧠 Skills Used

- **Natural Language Processing**
- **Speech Recognition**
- **Text-to-Speech Synthesis**
- **OpenAI GPT API Integration**
- **Computer Vision (OpenCV)**
- **Web App Development with Streamlit**
- **Python Programming**
- **Modular Code Design & GitHub Deployment**

---

## 🛠️ Tech Stack & Libraries

| Purpose                   | Library Used               | Notes                                                                 |
|--------------------------|----------------------------|-----------------------------------------------------------------------|
| Web UI                   | `streamlit`                | For quick prototyping and deployment                                 |
| NLP                      | `openai`                   | Used GPT models to respond intelligently to user prompts             |
| Speech to Text           | `speechrecognition`        | Converts spoken commands to text                                     |
| Text to Speech           | `pyttsx3`                  | Offline TTS engine for natural-sounding speech                       |
| CV (Camera + Detection)  | `opencv-python`            | Used for capturing webcam and basic object detection                 |
| Audio Handling           | `pyaudio` / `sounddevice`  | Initially used `pyaudio`, switched to `sounddevice` due to install issues on Windows |
| Environment Management   | `python-dotenv` (optional) | For securely loading API keys if needed                              |

---

## 🔄 Why I Switched Some Libraries

| Library             | Reason      |                                                                |
|---------------------|--------------------------|------------------------------------------------------------------------|
| `pyaudio` → `sounddevice` + `soundfile` | `pyaudio` is hard to install on some Windows setups; switched for smoother install |
| `gTTS` → `pyttsx3`  | `gTTS` requires internet and has latency; `pyttsx3` works offline and faster |
| `flask` (idea) → `streamlit` | Wanted faster prototyping with built-in UI components |

---


