# -*- coding: utf-8 -*-

##############
# Imports

import dash
import dash_core_components as dcc
import dash_html_components as html

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
                               html.Li(html.I(id='home')),
                               html.Li(html.A('Home', href='/')),
                               html.Li(html.I(id='videos')),
                               html.Li(html.A('Tutorial Videos', href='/apps/vid')),
                               html.Li(html.I(id='quizz')),
                               html.Li(html.A('AI practice', href='/apps/practice')), 
                               html.Li(html.I(id='competitions')),
                               html.Li(html.A('Current AI Competitions', href='/apps/competitions')), 
                               html.Li(html.I(id='news')),
                               html.Li(html.A('Medical AI News', href='/apps/news')),
                               html.Li(html.I(id='data')),
                               html.Li(html.A('Available Data Sets', href='/apps/data')),
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
#### Video tutorials
select the topic area you would like to know more about:

    ''')  
    ), 
    ),
    html.Div([
    dcc.Dropdown(
        id='vid_choice',
        options=[
            {'label': 'topic1', 'value': 'topic1'},
            {'label': 'topic2', 'value': 'topic2'},
            {'label': 'topic3', 'value': 'topic3'}
        ],
        value='topic1'
    ),
    html.Div(id='output-container')
])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)