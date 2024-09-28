import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Create a file handler
file_handler = logging.FileHandler('user_inputs.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

# Create a stream handler (for terminal output)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def main():
    st.title("Chatbot")
    # Add your chatbot logic here
    user_input = st.text_input("User Input", "")
    if user_input:
        response = "Hello, I am a chatbot. You said: " + user_input
        st.text_area("Bot Response", value=response, height=200)
        # Log the user input
        logger.info(f"User Input: {user_input}")

if __name__ == "__main__":
    main()