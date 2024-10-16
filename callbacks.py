from dash.dependencies import Input, Output, State
from dash import html
from services.bot_service import get_bot_response

def register_callbacks(app, db_handler):
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
                html.P(f"👤 {user_input}", style={'color': '#007BFF'}),
                html.P(f"🤖 {response}", style={'color': '#000000'})
            ]))
            return chat_history, ''
        return chat_history, ''