# AI Joke Agent

An AI-powered Joke Generator built using **Python, Streamlit, and Groq LLM**. This application generates fresh, dynamic jokes on any topic through natural language conversations instead of relying on predefined jokes.

---

## Features

* AI-powered joke generation using Groq LLM
* Interactive chat interface with Streamlit
* Conversation memory for contextual responses
* Supports jokes on any topic (students, programming, animals, teachers, etc.)
* Generates unique jokes on every request
* Clear chat option
* Secure API key management using `.env`

---

## Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.1 Instant Model
* Python Dotenv

---

## Project Structure

```text
AI-Joke-Agent/
│
├── main.py          # Streamlit application
├── tools.py         # Groq API integration
├── memory.py        # Conversation memory
├── prompts.py       # System prompt
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Joke-Agent.git
cd AI-Joke-Agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run the Application

```bash
streamlit run main.py
```

The application will open automatically in your browser.

---

## Example

**User**

> Tell me a joke about students.

**AI**

> Why did the student bring a ladder to school? Because the teacher said the test would be on a higher level!

---

## Future Enhancements

* Voice-enabled joke generation
* Multiple joke categories (Dad, Programming, Dark, Science, etc.)
* Joke rating system
* Persistent chat history
* Text-to-Speech support
* Multi-language joke generation

---

## Preview

Add screenshots of your Streamlit interface here after deployment.

---

## Author

**Sandhya Muruganand**

---

## 📄 License

This project is developed for learning and educational purposes.
