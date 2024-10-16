from models.chat_model import Chat
from utils.logger import configure_logger
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
MONGODB_URI = os.getenv('MONGODB_URI')

# Configure logging
logger = configure_logger('user_inputs.log')

class DBHandler:
    def __init__(self):
        # MongoDB connection
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client['ds-interview-bot']
        self.collection = self.db['chat-history']

    def retrieve_chat_history(self):
        chat_history = []
        for entry in self.collection.find().sort('timestamp'):
            chat_history.append({
                'user_input': entry['user_input'],
                'bot_response': entry['bot_response']
            })
        return chat_history

    def store_chat(self, user_input, bot_response):
        chat = Chat(user_input, bot_response)
        self.collection.insert_one({
            'timestamp': chat.timestamp,
            'user_input': chat.user_input,
            'bot_response': chat.bot_response
        })
        logger.info(f"User Input: {user_input}")
        logger.info(f"Bot Response: {bot_response}")

if __name__ == '__main__':
    db_handler = DBHandler()
    print("DBHandler initialized successfully.")

    # Store a chat entry
    user_input = "Hello, Neha?"
    bot_response = "Hello this is just an example of how to use db_handler class"
    db_handler.store_chat(user_input, bot_response)

    # Retrieve and print chat history
    chat_history = db_handler.retrieve_chat_history()
    for entry in chat_history:
        print(f"User: {entry['user_input']}")
        print(f"Bot: {entry['bot_response']}")
        print("-----")