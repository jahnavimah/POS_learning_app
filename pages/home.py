# Import necessary libraries 
import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

dash.register_page(__name__, path="/")

layout = html.Div([
    html.H1("", style={"color": "Green",'font-size':'44px','font-weight': 'bold',\
        'font-family': "Lucida Console",'text-align': 'center'}),
    html.Div([
        html.Div(id='gator', style={'width': '20%','height': 200,'background-image': 'url("/assets/gator.gif")',\
            "float":"left",'display': 'flex'}),
        
        dcc.Textarea(id='textarea-state-example1',
        value='',
        style={'width': '10%','height': 300,'background-color': 'White',\
              'font-size':'24px',"border":"None",'display':'inline-block',\
               "text-align": "justify",'padding': '20px'}),
        
        dcc.Textarea(id='textarea-state-example',
        value='Let us teach you Parts of Speech today',
        style={'width': '40%','height': 400,'background-color': 'LightYellow','color':'Purple',\
              'font-size':'24px',"border":"None",'display':'inline-block','box-shadow': '10px 10px 5px #aaaaaa',\
               "text-align": "justify",'padding': '20px'}),
        html.Div(id='hippo', style={'width': '13%','height': 200,'background-image': 'url("/assets/hippo.gif")',\
            "float":"right",'display': 'inline-block'})
        ]),
            ])

 


