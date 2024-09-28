import streamlit as st
import logging

# Configure logging
logging.basicConfig(filename='user_inputs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    st.title("Chatbot")
    # Add your chatbot logic here
    user_input = st.text_input("User Input", "")
    if user_input:
        response = "Hello, I am a chatbot. You said: " + user_input
        st.text_area("Bot Response", value=response, height=200)
        # Log the user input
        logging.info(f"User Input: {user_input}")

if __name__ == "__main__":
    main()