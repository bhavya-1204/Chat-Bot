# app.py

import streamlit as st
from agent_setup import create_chat_agent

st.set_page_config(page_title="LangChain Chatbot", page_icon="🤖")
st.title("🤖 LangChain Chatbot (Groq 120B)")

# Create agent once and store in session state
if "agent" not in st.session_state:
    st.session_state.agent = create_chat_agent()

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):

    # Add user message to UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.agent.invoke(
                    {"messages": [{"role": "user", "content": prompt}]},
                    {"configurable": {"thread_id": "1"}}
                )

                reply = response["messages"][-1].content

                st.markdown(reply)

                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )

            except Exception as e:
                st.error(f"Error: {e}")
