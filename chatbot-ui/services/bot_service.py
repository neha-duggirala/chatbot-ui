# Define a simple rule-based chatbot response function
def get_bot_response(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input:
        return "Hi there! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"