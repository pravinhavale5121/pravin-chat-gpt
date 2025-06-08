import streamlit as st
import openai
import os

# Set API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Chat AI with Streamlit & OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Text input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    ai_message = response['choices'][0]['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": ai_message})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")
