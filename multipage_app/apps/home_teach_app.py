# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from app import app

# image_directory = '/Users/Dell/Documents/Hackathon 2019/Hackathon-2019/Hackathon-2019/multipage_app/apps/images'
 
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
## Breaking Open the Black Box
At the 2019 Mount Sinai Health Hackathon we set about to making AI more accesible to those working in a healthcare setting
This website provides access to explanations of AI tools used in the health care setting today as well as the concepts behind these tools


### Quickstart: select whether you want to explore existng AI tools in medicine or explanations of AI topics
    '''),
            style={'padding': 100} ),
    ),
    html.Div(
        children=[
            html.Center(
            dcc.Markdown('''
                ### What is this website?
            '''),style={'padding-top': 50}),
            html.Center(
            dcc.Markdown('''
                ##### The healthcare field needs more tech-savvy professionals, like you, to understand and smartly leverage Artificial Intelligence (AI) technology.
                        '''),
            style={'padding': 100}
        )],style={
        'backgroundColor':'#f1f0ea',
        'border': 'grey',
        'padding': '50px 10px 50px'}
    ),
    html.Center(
        children=[
        html.A([
            html.Img(
                    src='https://i.imgur.com/BV0MYj2.png',
                    style={
                        'height' : '35%',
                        'width' : '35%',
                        'float' : 'center',
                        'position' : 'relative',
                        'padding-top' : 0,
                        'padding-right' : 0,
                        'padding' : 40,
                        'border-radius': '100px'
                    })], href='/apps/tool'),
        html.A([
            html.Img(
                    src='https://i.imgur.com/L4neq6h.png',
                    style={
                        'height' : '35%',
                        'width' : '35%',
                        'float' : 'center',
                        'position' : 'relative',
                        'padding-top' : 0,
                        'padding-right' : 0,
                        'padding': 40,
                        'border-radius': '100px'
            })], href='/apps/vid')]
    #         # dcc.Link(html.Button('Existing AI healthcare tools'), href='/apps/tool', style={'padding': 100})
    )

    ]
)

# if __name__ == '__main__':
#     app.run_server(debug=True)