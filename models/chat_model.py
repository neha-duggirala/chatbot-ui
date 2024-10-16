from datetime import datetime

class Chat:
    def __init__(self, user_input, bot_response):
        self.user_input = user_input
        self.bot_response = bot_response
        self.timestamp = datetime.now().strftime('%Y-%m-%d')