import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import logging
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
MONGODB_URI = os.getenv('MONGODB_URI')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Create a file handler
file_handler = logging.FileHandler('user_inputs.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(file_handler)

# Initialize the Dash app
app = dash.Dash(__name__)

# MongoDB connection
client = MongoClient(MONGODB_URI)
db = client['ds-interview-bot']
collection = db['chat-history']

# Function to retrieve chat history from MongoDB
def retrieve_chat_history():
    chat_history = []
    for entry in collection.find().sort('timestamp'):
        chat_history.append(html.Div([
            html.P(f"User: {entry['user_input']}", style={'color': '#007BFF'}),
            html.P(f"Bot: {entry['bot_response']}", style={'color': '#000000'})
        ]))
    return chat_history

# Define the layout of the app
app.layout = html.Div([
    html.Div([
        html.H1("Chatbot", style={'textAlign': 'center', 'color': '#007BFF'}),
        html.Div(id='chat-window', children=retrieve_chat_history(), style={
            'height': '400px', 'overflowY': 'scroll', 'border': '1px solid #007BFF', 'padding': '10px', 'borderRadius': '5px', 'backgroundColor': '#F8F9FA'
        }),
        html.Div([
            dcc.Input(id='user-input', type='text', placeholder='Type your message here...', style={
                'width': '80%', 'padding': '10px', 'fontSize': '16px', 'borderRadius': '5px', 'border': '1px solid #007BFF'
            }),
            html.Button('Send', id='submit-button', n_clicks=1, style={
                'padding': '10px 20px', 'fontSize': '16px', 'borderRadius': '5px', 'border': 'none', 'backgroundColor': '#007BFF', 'color': 'white', 'marginLeft': '10px'
            }),
        ], style={'display': 'flex', 'justifyContent': 'center', 'marginTop': '20px'}),
    ], style={'maxWidth': '800px', 'margin': '0 auto', 'padding': '20px', 'border': '1px solid #007BFF', 'borderRadius': '10px', 'backgroundColor': '#FFFFFF', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'})
], style={'backgroundColor': '#F0F2F5', 'padding': '50px 0'})

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
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Log the user input and bot response
        logger.info(f"User Input: {user_input}")
        logger.info(f"Bot Response: {response}")
        # Store the chat in MongoDB
        collection.insert_one({
            'timestamp': timestamp,
            'user_input': user_input,
            'bot_response': response
        })
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