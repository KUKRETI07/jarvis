
             # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 


# def process_command(command):
#     command = command.lower()  
#     if "hey jarvis" in command:
#         return "Hello boss, how can I help you?"
#     elif "who are you jarvis " in command:
#         return "I am your personal assistant, Mini Jarvis."
#     elif "what can you do" in command:
#         return "Right now, I can listen and talk. Soon I will see and think too!"
#     elif "exit" in command or "bye" in command:
#         return "Goodbye boss, have a great day."
#     else:
#         return "Sorry boss, I didn’t get that yet."
    

# # utils/nlp.py
# import datetime
# import random

# # Basic memory - temporary (can be upgraded later)
# context_memory = []

# def process_command(command):
#     command = command.lower().strip()
#     context_memory.append(command)

#     # Basic understanding logic
#     if "your name" in command:
#         return "I am Jarvis, your personal AI assistant."

#     elif "time" in command:
#         now = datetime.datetime.now().strftime("%I:%M %p")
#         return f"The current time is {now}."

#     elif "date" in command:
#         today = datetime.date.today().strftime("%B %d, %Y")
#         return f"Today's date is {today}."

#     elif "joke" in command:
#         jokes = [
#             "Why did the computer go to therapy? Because it had a hard drive.",
#             "I told my AI friend a joke about UDP... but I'm not sure if it got it.",
#             "I asked the neural network to predict my future. It said: '404 future not found.'"
#         ]
#         return random.choice(jokes)

#     elif "remember" in command:
#         if "what" in command:
#             if context_memory:
#                 return f"You recently said: '{context_memory[-2]}'"
#             else:
#                 return "I don’t have anything in memory yet."
#         else:
#             return "Noted. I'll remember that for now."

#     elif "exit" in command or "shutdown" in command:
#         return "Shutting down Jarvis. Goodbye boss."

#     else:
#         return "I'm still learning. Can you repeat or rephrase that?"


# print(response.choices[0].message.content)


# utils/nlp.py

import os
import requests


# GROQ_API_KEY = "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"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-70b-8192"  # Latest supported one (Mixtral is deprecated)

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def process_command(user_input, personality="You are a helpful, kind, emotionally intelligent AI assistant."):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": personality},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_ENDPOINT, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content'].strip()
    except requests.exceptions.HTTPError as e:
        return f"[Error] HTTP Error: {e}"
    except Exception as e:
        return f"[Error] {str(e)}"

