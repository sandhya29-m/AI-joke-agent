import streamlit as st

from prompts import SYSTEM_PROMPT
from memory import ConversationMemory
from tools import generate_joke

st.set_page_config(
    page_title="😂 AI Joke Agent",
    page_icon="😂"
)

st.title("😂 AI Joke Agent")

st.write("Ask me for jokes on any topic!")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "chat" not in st.session_state:
    st.session_state.chat = []

for message in st.session_state.chat:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Tell me a joke...")

if prompt:

    st.session_state.chat.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.memory.get_history())

    messages.append({
        "role": "user",
        "content": prompt
    })

    reply = generate_joke(messages)

    st.session_state.memory.add("user", prompt)
    st.session_state.memory.add("assistant", reply)

    st.session_state.chat.append({
        "role": "assistant",
        "content": reply
    })

    with st.chat_message("assistant"):
        st.markdown(reply)

if st.sidebar.button("Clear Chat"):

    st.session_state.chat = []
    st.session_state.memory.clear()
    st.rerun()