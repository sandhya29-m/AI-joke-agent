from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.1-8b-instant"

def generate_joke(messages):

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.9,
        max_tokens=300
    )

    return response.choices[0].message.content