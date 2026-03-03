# 🤖 Simple LangChain Chatbot (Groq + Streamlit)

A minimal conversational AI chatbot built with:

* **LangChain Agents**
* **LangGraph InMemorySaver (session memory)**
* **Groq `openai/gpt-oss-120b`**
* **Streamlit**

This project demonstrates how to create a clean, session-based AI chatbot using modern LangChain architecture.

---

## 🚀 Features

* 💬 Clean Streamlit chat interface
* 🧠 In-memory conversation history (per session)
* ⚡ Powered by Groq `gpt-oss-120b`
* 🧩 Modular agent setup
* 🪶 Lightweight and beginner-friendly

> Note: This is a basic chatbot. It does **not** include file upload, image upload, RAG, or external tools.

---

## 📁 Project Structure

```
your_project/
│
├── app.py              # Streamlit UI
├── agent_setup.py      # Agent configuration
└── README.md
```

---

## 🧠 Agent Setup

The chatbot agent is created using:

```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model="groq:openai/gpt-oss-120b",
    system_prompt=SYSTEM_PROMPT,
    checkpointer=InMemorySaver()
)
```

Conversation memory is stored using `InMemorySaver()` and persists during the user session.

---

## ⚙️ Installation

### 1️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 2️⃣ Install dependencies

```bash
pip install streamlit langchain langgraph groq
```

---

## 🔑 Environment Variable

Set your Groq API key:

### macOS/Linux

```bash
export GROQ_API_KEY="your_api_key_here"
```

### Windows (PowerShell)

```powershell
setx GROQ_API_KEY "your_api_key_here"
```

Restart your terminal after setting the key.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## 🛠 How It Works

1. User types a message in Streamlit.
2. The message is sent to the LangChain agent.
3. The agent processes it using Groq `gpt-oss-120b`.
4. Memory is maintained during the session.
5. The response is displayed in the chat interface.

---

## 📌 Requirements

* Python 3.9+
* Groq API key
* Internet connection

---

## 📜 License

MIT License
