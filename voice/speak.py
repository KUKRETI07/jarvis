         # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 


# import pyttsx3         # Python library for offline text-to-speech conversion 

# def speak(text):
#     print("Jarvis:", text)
    
#     try:
#         engine = pyttsx3.init()            # Sets up the speech engine before generating audio.
#         engine.setProperty('rate', 170)    # Speed of speech
#         engine.setProperty('volume', 1.0)   # Volume (0 to 1)
#         engine.say(text)               # Prepares the speech output
#         engine.runAndWait()          # Blocks the program until the speech is complete.
#     except Exception as e:
#         print("[ERROR] Voice engine failed:", e)    


from gtts import gTTS
import pygame
import os
from textblob import TextBlob

def speak(text):
    print("Jarvis:", text)

    # Analyze sentiment
    sentiment = TextBlob(text).sentiment.polarity

    # Voice style based on sentiment
    if sentiment > 0.3:
        tld = 'com.au'  # Happy
        slow = False
    elif sentiment < 0.3:
        tld = 'co.uk'  # Serious
        slow = True
    else:
        tld = 'co.uk'  # Neutral
        slow = False

    try:
        tts = gTTS(text=text, lang='en', tld=tld, slow=slow)
        tts.save("temp.mp3")

        # Play the audio
        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Clean up after speaking
        pygame.mixer.quit()
        os.remove("temp.mp3")

    except Exception as e:
        print("[ERROR] Voice system failed:", e)
