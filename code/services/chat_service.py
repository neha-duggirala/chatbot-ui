from db_handler import DBHandler

class ChatService:
    def __init__(self):
        self.db_handler = DBHandler()

    def store_chat(self, user_input, bot_response):
        self.db_handler.store_chat(user_input, bot_response)

    def retrieve_chat_history(self):
        return self.db_handler.retrieve_chat_history()