import streamlit as st
import ollama

# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "qwen3:4b"

st.set_page_config(
    page_title="Local Ollama Chatbot",
    page_icon="🤖"
)

st.title("🤖 Chatbot using Ollama in Local System")
st.caption(f"Model Name: {MODEL_NAME}")


# -----------------------------
# Initialize chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Clear Chat Button
# -----------------------------
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()


# -----------------------------
# Display previous messages
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask me anything...")


if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = ollama.chat(
                    model=MODEL_NAME,
                    messages=st.session_state.messages
                )

                assistant_reply = response["message"]["content"]

            except Exception as e:
                assistant_reply = f"❌ Error: {str(e)}"

        st.markdown(assistant_reply)

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_reply
    })