import openai
import streamlit as st
import os
from dotenv import load_dotenv

def chat_page():
    load_dotenv()
    st.title("AI Attorney")
    st.markdown("Chat With Me About your Problems and laws!!")

    # Set your OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the model and message history in session state
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Take user input for new message
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Fetch the response from OpenAI using the chat API
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Use the ChatCompletion API to handle the response
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],  # Use the selected model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *st.session_state.messages  # Include the message history in the prompt
                ],
                max_tokens=150,  # Set the token limit for the response
                temperature=0.7,  # Adjust the temperature for response creativity
            )
            full_response = response['choices'][0]['message']['content'].strip()  # Extract the assistant's response
            message_placeholder.markdown(full_response)  # Display the full response

        # Append the assistant's response to the session state message history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    chat_page()
