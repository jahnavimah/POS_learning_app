from dash import dcc
from dash import html

from dash.dependencies import Input, Output
#import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import home,main


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div([html.Div('KizingoBox',style={'padding-left': '20px','font-family': 'Arial', \
    'font-weight': 'bold','font-size':'30px','color':'Purple','display':'inline-block'}),
        dcc.Link('Home|', href='/apps/home',style={'padding-left': '950px','font-family': 'Arial', \
    'font-weight': 'bold','font-size':'20px','display':'inline-block'}),
        dcc.Link('Play', href='/apps/main',style={'font-family': 'Arial', \
    'font-weight': 'bold','font-size':'20px','display':'inline-block'}),
    ], className="column"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/home':
        return home.layout
    if pathname == '/apps/main':
        return main.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=False)