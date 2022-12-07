# Import necessary libraries 
import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from app import app


layout = html.Div([
    html.H1("", style={"color": "Green",'font-size':'44px','font-weight': 'bold',\
        'font-family': "Arial",'text-align': 'center'}),
    html.Div([
        html.Div(id='gator', style={'width': 900,'height': 661,'background-image': 'url("/assets/homepage3.jpg")',\
            'border': '8px ridge blue','display': 'block','margin': '0 auto'}),
            ]),
])
 


