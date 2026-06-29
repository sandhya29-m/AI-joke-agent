import os
from groq import Groq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Use Streamlit Secrets if available
if not api_key:
    api_key = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=api_key)

MODEL = "llama-3.1-8b-instant"

def generate_joke(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.9,
        max_tokens=300
    )

    return response.choices[0].message.content
