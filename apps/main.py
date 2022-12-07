import spacy
import pandas as pd
import dash
from dash import Dash, dcc, html,callback
from dash.dependencies import Input, Output, State
from app import app

import re

nlp = spacy.load("en_core_web_sm")

layout = html.Div([
    html.H1("", style={"color": "BLue",'font-size':'16px'}),
    html.Div([
    html.Div([
    dcc.Textarea(
        id='textarea-state-example',
        value='Enter text here',
        style={'width': '45%','height': 300,'background-color':'LightYellow','border': '3px ridge purple','color':'Purple',\
              'font-size':'16px','display': 'inline-block',"line-height": "30px",'font-weight': 'bold',\
              'font-family': 'Arial','margin-left': '20px'}),
    html.Div(id='area', style={'width': '45%','height': 300,'display': 'inline-block'}),
             ]),

    html.Div([ 
    html.Button('Submit', id='textarea-state-example-button', n_clicks=0,\
                style={"background-color":"Purple","border": "none","color": "Yellow","padding": "5px 15px",\
                       "text-align": "center","font-size": "16px",'font-weight': 'bold',\
                       'font-family': 'Arial','margin-left': '20px','display': 'inline-block'}),
    html.Div(id='right_area', style={'height': 116,'width':350,
                                     'background-image': 'url("/assets/labelsformatted.jpg")',\
                                    'right': '100px','position': 'Absolute',\
                                     'margin-right':'80px','display': 'inline-block'
                                    }),
        ]),
    html.Br(),
    html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line','color':'Green','font-size':'16px',\
                                                        'margin-left': '20px',\
                                                        "line-height": "30px",'font-weight': 'bold','font-family': 'Arial'}), 
    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Dropdown(id='my-button',
               options=[
                   {'label':'Noun','value':'NOUN','className':"optionA"},
                   {'label':'Proper Noun','value':'PROPN','className':"optionB"},
                   {'label':'Pronoun','value':'PRON','className':"optionC"},
                   {'label':'Verb','value':'VERB','className':"optionD"},
                   {'label':'Adjective','value':'ADJ','className':"optionE"},
                   {'label':'Adverb','value':'ADV','className':"optionF"}          
               ],
               value='',className="select_box",
                multi=True,placeholder="Select a POS TAG", 
                style={"background-color":"LightYellow","border": "none",'font-family': 'Arial','margin-left': '20px','margin-right': '50px'}),

    ]),
   
    
],style={'overflow': 'scroll',
          'background-size': '100%',
          'position': 'fixed',
          'width': '100%',
          'height': '100%','background-image': 'url("/assets/stars.png")'
          })


@callback(
    Output('textarea-state-example-output', 'children'),Output('area', 'children'),
    Input('textarea-state-example-button', 'n_clicks'),State('textarea-state-example', 'value'),
    Input('my-button', 'value')
)

   
def update_output(n_clicks,value, value0):
    if n_clicks > 0:
        doc = nlp(value)

        lst=[]
        for token in doc:
            ls=[token.text, token.lemma_, token.pos_, token.tag_, token.dep_,\
                token.shape_, token.is_alpha, token.is_stop][0:3]
            del ls[1:2]
            lst.append(ls)
            
        df=pd.DataFrame(lst,columns=['text','pos'])
        p=dict(df.values)
        
        pp=dict(zip([k for k,v in p.items() if v in value0], [v for k,v in p.items() if v in value0]))

        colour={'NOUN':{"background-color": "Yellow", "color": "black"},'PROPN':{"background-color": "Blue", "color": "white"},\
                'PRON':{"background-color": "Magenta", "color": "black"},'VERB':{"background-color": "Green", "color": "white"},\
                'ADJ':{"background-color": "Red", "color": "white"},'ADV':{"background-color": "LightBlue", "color": "black"}}
        #colour={'NOUN':{"color": "Blue"},'PROPN':{ "color": "Mauve"},\
                #'PRON':{"color": "Magenta"},'VERB':{"color": "Green"},\
                #'ADJ':{"color": "Red"},'ADV':{"color": "LightBlue"}}

        if bool(value0):
            xx=[k for k,v in pp.items() if v in value0]
            value1=re.split('(\W+)', value)
            value1=[x for x in value1 if x!='']
            db=[]
            rt1=[]
            for c,h in enumerate(xx):
                txt=[h==n for n in value1]
                value2=pd.DataFrame(value1,columns={'text'})
                booleans1=pd.DataFrame(txt,columns={'booleans'})
                tot=pd.concat([value2,booleans1],axis=1)

                ggh=[]
                for i,row in tot.iterrows():
                    if row['booleans']==True:
                        gg=[v for k,v in pp.items() if k == row['text']]
                    else:
                        gg=['']
                    ggh.append(gg)

                ggh=[x for xs in ggh for x in xs]
                tot['POS']=ggh 

                output = html.Div([value])
                seq=[]
                for i,row in tot.iterrows():

                    if row['booleans']==True:
                        d=html.Mark(row['text'],style=colour[row['POS']])
                    else:
                        d=row['text']
                    seq.append(d)
                db.append(seq)


                #db1=[]
                #for d in db:
                    #dbb=list(set(d))
                    #db1.append(dbb)
                db1=[list(set(d)) for d in db]

                rt=[]
                for j in range(len(db[0])):
                    n=[db[i][j] for i in range(len(db))]
                    n=list(set(n))
                    if all(isinstance(x, str) for x in n)==False:
                        n=[i for i in n if type(i)!=str]
                    rt.append(n)

                rt1=[x for xs in rt for x in xs]
                

            output.children = rt1

            return 'You have entered your text',\
        html.Div([html.Div(output,style={'width': '100%','height': 300,'overflow': 'scroll',\
                              'margin-left': '50px',
                              'font-size':'16px',"line-height": "30px",'font-weight': 'bold','font-family': 'Arial',\
                              'background-color':'LightYellow','border': '3px ridge purple'})])
        else:
            return [''],['']
    
    else:
        return [''],['']



