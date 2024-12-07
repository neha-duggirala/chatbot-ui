from dash import dcc, html

# Function to retrieve chat history from DBHandler
def retrieve_chat_history(db_handler):
    chat_history = []
    for entry in db_handler.retrieve_chat_history():
        chat_history.append(html.Div([
            html.P(f"User: {entry['user_input']}", style={'color': '#007BFF'}),
            html.P(f"Bot: {entry['bot_response']}", style={'color': '#000000'})
        ]))
    return chat_history

# Define the layout of the app
def create_layout(db_handler):
    return html.Div([
        html.Div([
            html.H1("Chatbot", style={'textAlign': 'center', 'color': '#007BFF'}),
            html.Div(id='chat-window', children=retrieve_chat_history(db_handler), style={
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