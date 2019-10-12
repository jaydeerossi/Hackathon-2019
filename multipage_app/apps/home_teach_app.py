# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app

 
#############
# Layout

layout = html.Div(
    id='main-page-content',children= [
    html.Div(
        children=[
            #nav bar
            html.Nav(
                #inside div
                html.Div(
                    children=[
                        html.A(
                            'Website Name',
                            style={'margin':15, 'fontSize':30}
                        ),
                        #ul list components
                        html.Ul(
                            children=[
                               html.Li(html.A('Home', href='/')),
                               html.Li(html.A('Search by Specialty', href='/apps/organ')),
                               html.Li(html.A('Tool Lookup', href='/apps/tool')),
                               html.Li(html.A('Tutorial Videos', href='/apps/vid')),
                               html.Li(html.A('Data Sets', href='/apps/data')),
                            ],
                            id='nav-mobile',
                            className='right hide-off-med-and-down'
                        ), 
                    ],
                    className='nav-wrapper'
                ),style={'background-color':'#4c586f'}),
        ],
        className='navbar-fixed'
    ),
    html.Div(
        html.Center(
        dcc.Markdown('''
## Welcome to the World of Artificial Intelligence
At the 2019 Mount Sinai Health Hackathon we set about to making AI more accesible to those working in a healthcare setting
This website provides access to explanations of AI tools used in the health care setting today as well as the concepts behind these tools


### Quickstart: select whether you want to explore exisitng AI tools in medicine or explainations of AI topics
    '''),  
    # ![](static/aiBrain.png)
    #Image courtesy of Getty Images

    ),
    # style={
        # 'backgroundColor':'#f1f0ea',
        # 'border': 'grey',
        #'padding': '6px 0px 0px 8px'
        # 'background-image': static/aiBrain.png}
    ),
    dcc.Link(html.Button('Videos on topics in AI'), href='/apps/vid'),
    dcc.Link(html.Button('Existing AI healthcare tools'), href='/apps/tool')
    ])

# if __name__ == '__main__':
#     app.run_server(debug=True)