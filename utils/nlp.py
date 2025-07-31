
#              # NOTE: COMMENTED PART ARE THE PREVIOUS CODES THAT I USED PREVIOUSLY 


# # def process_command(command):
# #     command = command.lower()  
# #     if "hey jarvis" in command:
# #         return "Hello boss, how can I help you?"
# #     elif "who are you jarvis " in command:
# #         return "I am your personal assistant, Mini Jarvis."
# #     elif "what can you do" in command:
# #         return "Right now, I can listen and talk. Soon I will see and think too!"
# #     elif "exit" in command or "bye" in command:
# #         return "Goodbye boss, have a great day."
# #     else:
# #         return "Sorry boss, I didn’t get that yet."
    

# # # utils/nlp.py
# # import datetime
# # import random

# # # Basic memory - temporary (can be upgraded later)
# # context_memory = []

# # def process_command(command):
# #     command = command.lower().strip()
# #     context_memory.append(command)

# #     # Basic understanding logic
# #     if "your name" in command:
# #         return "I am Jarvis, your personal AI assistant."

# #     elif "time" in command:
# #         now = datetime.datetime.now().strftime("%I:%M %p")
# #         return f"The current time is {now}."

# #     elif "date" in command:
# #         today = datetime.date.today().strftime("%B %d, %Y")
# #         return f"Today's date is {today}."

# #     elif "joke" in command:
# #         jokes = [
# #             "Why did the computer go to therapy? Because it had a hard drive.",
# #             "I told my AI friend a joke about UDP... but I'm not sure if it got it.",
# #             "I asked the neural network to predict my future. It said: '404 future not found.'"
# #         ]
# #         return random.choice(jokes)

# #     elif "remember" in command:
# #         if "what" in command:
# #             if context_memory:
# #                 return f"You recently said: '{context_memory[-2]}'"
# #             else:
# #                 return "I don’t have anything in memory yet."
# #         else:
# #             return "Noted. I'll remember that for now."

# #     elif "exit" in command or "shutdown" in command:
# #         return "Shutting down Jarvis. Goodbye boss."

# #     else:
# #         return "I'm still learning. Can you repeat or rephrase that?"


# # print(response.choices[0].message.content)


# # utils/nlp.py

# import os
# import requests
# import openai

# from dotenv import load_dotenv
# load_dotenv()  

# openai.api_key = os.getenv("API_KEY")  
# openai.api_base = "https://api.openai.com/v1"

# print("API_KEY:", os.getenv("API_KEY"))

# GROQ_ENDPOINT = "https://api.openai.com/v1/chat/completions"
# MODEL = "GPT-3.5 Turbo"  # Latest supported one (Mixtral is deprecated)

# HEADERS = {
#     "Authorization": f"Bearer {openai.api_key}",
#     "Content-Type": "application/json"
# }

# def process_command(user_input, personality="You are a helpful, kind, emotionally intelligent AI assistant."):
#     payload = {
#         "model": MODEL,
#         "messages": [
#             {"role": "system", "content": personality},
#             {"role": "user", "content": user_input}
#         ],
#         "temperature": 0.7
#     }

#     try:
#         response = requests.post(GROQ_ENDPOINT, headers=HEADERS, json=payload)
#         response.raise_for_status()
#         data = response.json()
#         return data['choices'][0]['message']['content'].strip()
#     except requests.exceptions.HTTPError as e:
#         return f"[Error] HTTP Error: {e}"
#     except Exception as e:
#         return f"[Error] {str(e)}"

import os
import cohere
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key from the .env file
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Initialize the Cohere client
co = cohere.Client(COHERE_API_KEY)

# Function to process natural language command using Cohere
def process_command(user_input, personality="You are a helpful AI assistant."):
    try:
        response = co.chat(
            message=user_input,
            model="command-r-plus",  # Use command-r or command-r-plus (latest, best for chat)
            temperature=0.7,
            chat_history=[],
            prompt_truncation="AUTO",
        )
        return response.text.strip()
    except cohere.CohereAPIError as e:
        return f"[Cohere API Error] {str(e)}"
    except Exception as e:
        return f"[Error] {str(e)}"
