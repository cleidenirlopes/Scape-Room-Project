import dash
from dash import dcc
from dash import html
import base64

# Path to your background image
BACKGROUND_IMAGE_PATH = 'D:/Project/Scape Room Project/Scape-Room-Project/bg.com.png'

def encode_image(image_path):
    with open(image_path, 'rb') as b64_file:
        encoded_string = base64.b64encode(b64_file.read()).decode('utf-8')
    return f'data:image/png;base64,{encoded_string}'

encoded_background = encode_image(BACKGROUND_IMAGE_PATH)

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundImage': f'url("{encoded_background}")',
        'backgroundSize': 'cover',
        'height': '100vh',
        'margin': '0',
        'padding': '0',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center',
        'justifyContent': 'center',
        'color': 'white',  # Default text color on the background
    },
    children=[
        html.H1("Welcome to the Scape Room!"),
        html.Div(
            style={'padding': '20px', 'backgroundColor': 'rgba(0, 0, 0, 0.5)', 'borderRadius': '10px'},
            children=[
                html.P("This is the main content area."),
                dcc.Input(placeholder="Enter your name"),
                html.Button("Submit", id="submit-button"),
                html.Div(id="output-div"),
            ]
        ),
        html.Div(
            style={'position': 'absolute', 'bottom': '20px', 'left': '20px', 'backgroundColor': 'rgba(0, 0, 0, 0.7)', 'padding': '10px', 'borderRadius': '5px'},
            children=[
                html.P("Side Container Content", style={'margin': '0'}),
            ]
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)