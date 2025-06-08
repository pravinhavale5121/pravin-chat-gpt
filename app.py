import streamlit as st
import openai
import os

# Use your OpenAI API key (we'll set it later)
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🤖 My Chat AI")

# Save chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input box
user_input = st.text_input("You:", "")

# When user sends message
if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Ask OpenAI to generate reply
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4o"
        messages=st.session_state.messages
    )

    reply = response["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Show all messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")
