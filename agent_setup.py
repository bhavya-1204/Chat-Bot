# agent_setup.py

from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer clearly and concisely.
"""

def create_chat_agent():
    agent = create_agent(
        model="groq:openai/gpt-oss-120b",
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver()
    )
    return agent
