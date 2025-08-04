import os
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

#  Groq API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

# Raise error if API key is not set
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please set it before running.")

# Initialize Groq client
client = Groq(api_key=api_key)

# Main function to process user commands
def process_command(user_input, personality="You are a helpful AI assistant "):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # You can switch to 70b if needed
            messages=[
                {"role": "system", "content": personality},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"[ Error] {str(e)}"
