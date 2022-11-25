# Import necessary libraries 
import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from app import app


layout = html.Div([
    html.H1("", style={"color": "Green",'font-size':'44px','font-weight': 'bold',\
        'font-family': "Lucida Console",'text-align': 'center'}),
    html.Div([
        html.Div(id='gator', style={'width': '30%','height': 500,'background-image': 'url("/assets/gator.gif")',\
            "float":"left",'display': 'inline-block'}),
        
        dcc.Textarea(id='textarea-state-example1',
        value='',
        style={'width': '0.2%','height': 400,'background-color': 'White',\
              'font-size':'24px',"border":"None",'display':'inline-block',\
               "text-align": "justify",'padding': '20px','display': 'inline-block'}),
        
        dcc.Textarea(id='textarea-state-example',
        value='Parts of Speech\n\nNoun: A word to identify people, places, things and names\
        \n\nVerb: A word to describe an action\n\nAdjective: A word that describes a noun\n\nAdverb: A word that describes a verb\n\nPronoun: A word that refers to a noun',

        style={'width': '30%','height': 400,'background-color': 'LightYellow','color':'Purple',\
              'font-size':'24px',"border":"None",'display':'inline-block','box-shadow': '10px 10px 5px #aaaaaa',\
               "text-align": "justify",'padding': '20px','font-family': 'Times New Roman, Times, serif',\
               'font-weight': 'bold','display': 'inline-block'}),
        html.Div(id='hippo', style={'width': '30%','height': 500,'background-image': 'url("/assets/hippo.gif")',\
            "float":"right",'display': 'inline-block'})
        ]),
            ])

 


