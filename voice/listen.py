            # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 

# import speech_recognition as sr
# def listen_command():
#     recognizer = sr.Recognizer()   # Creates an instance of the Recognizer class, which handles speech recognition.
#     with sr.Microphone() as source:     #  Initializes the microphone as the audio source.
#         print("Listening...")
#         audio = recognizer.listen(source)   # listen your voice and store it into audio variable 

#         try:
#             command = recognizer.recognize_google(audio)
#             print(" You said:", command)
#             return command.lower()
#         except sr.UnknownValueError:
#             print("Sorry, I couldn't understand.")
#             return ""
#         except sr.RequestError:
#             print(" Could not request results from Google Speech Recognition service.")
#             return ""


import speech_recognition as sr
import time

def listen_command(timeout=2, pause_threshold=2):
    r = sr.Recognizer()
    r.pause_threshold = pause_threshold  # Seconds of silence before considering speech ended
    
    with sr.Microphone() as source:
        print("Listening... (Speak now)")
        try:
            # Adjust for ambient noise once
            r.adjust_for_ambient_noise(source, duration=1)
            
            # Listen with extended timeout
            audio = r.listen(source, timeout=timeout)
            
            # If we get here, speech was detected
            command = r.recognize_google(audio).lower()
            return command
            
        except sr.WaitTimeoutError:
            print(f"No speech detected for {timeout} seconds")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

