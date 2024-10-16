import dash
from dash.dependencies import Input, Output, State
from db_handler import DBHandler
from layout import create_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__)

# Initialize the DBHandler
db_handler = DBHandler()

# Set the layout of the app
app.layout = create_layout(db_handler)

# Register callbacks
register_callbacks(app, db_handler)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)