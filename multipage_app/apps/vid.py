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
#### Video tutorials
search for the topic area you would like to know more about or browse available videos:
    ''')  
    ),
    ),
    dcc.Input(
        type='text',
        value = '',
        placeholder= 'Type the name of the tool here and press submit',
        style={
            'margin':30,
            'width': '50%'
        }
    ),
    html.Button('Submit', id='submit'),
    html.Div([
    # html.Video(src='static/test_vid.mov'),
    html.Div(id='output-container')
])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)