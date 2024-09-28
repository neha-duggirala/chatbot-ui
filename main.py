import streamlit as st

def main():
    st.title("Chatbot")
    # Add your chatbot logic here
    user_input = st.text_input("User Input", "")
    if user_input:
        response = "Hello, I am a chatbot. You said: " + user_input
        st.text_area("Bot Response", value=response, height=200)

if __name__ == "__main__":
    main()