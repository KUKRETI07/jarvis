import queue
import sounddevice as sd
import vosk
import json

model = vosk.Model(r"models/vosk-model-small-en-us-0.15")
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen_for_wake_word():
    print(" Passive listener started... Say 'Jarvis' to activate.")

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                if "hello" in text:
                    print(" Wake word 'Jarvis' detected!")
                    return  # Wake up Jarvis
