from dash import html
import dash
from dash.dependencies import Input, Output, State
from db_handler import DBHandler
from layout import create_layout

# Initialize the Dash app
app = dash.Dash(__name__)

# Initialize the DBHandler
db_handler = DBHandler()

# Set the layout of the app
app.layout = create_layout(db_handler)

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

# Define the callback to update the chat window and clear the input field
@app.callback(
    [Output('chat-window', 'children'), Output('user-input', 'value')],
    [Input('submit-button', 'n_clicks')],
    [State('user-input', 'value'), State('chat-window', 'children')]
)
def update_chat(n_clicks, user_input, chat_history):
    if chat_history is None:
        chat_history = []
    if n_clicks > 0 and user_input:
        response = get_bot_response(user_input)
        # Store the chat in MongoDB
        db_handler.store_chat(user_input, response)
        # Update chat history
        chat_history.append(html.Div([
            html.P(f"User: {user_input}", style={'color': '#007BFF'}),
            html.P(f"Bot: {response}", style={'color': '#000000'})
        ]))
        return chat_history, ''
    return chat_history, ''

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)