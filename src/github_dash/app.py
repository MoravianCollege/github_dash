# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from redis import Redis

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

def get_last_update_time():
    r = Redis()
    return r.get('last_update').decode()


def get_next_update_time():
    r = Redis()
    return r.get('next_update').decode()


def get_used_api_calls():
    r = Redis()
    return r.get('used').decode()


def get_remaining_api_calls():
    r = Redis()
    return r.get('remaining').decode()


def make_stacked_bar_plot(repo_name):
    r = Redis()
    repo = eval(r.get(repo_name))

    return dcc.Graph(
        id='{}-graph'.format(repo_name),
        figure={
            'data': [
                {'x': repo['names'], 'y': repo['comments'], 'type': 'bar', 'name': 'Comments'},
                {'x': repo['names'], 'y': repo['merges'], 'type': 'bar', 'name': 'Merges'},
                {'x': repo['names'], 'y': repo['closed_pull_requests'], 'type': 'bar',
                 'name': 'Closed Pull Requests'},
                {'x': repo['names'], 'y': repo['open_pull_requests'], 'type': 'bar',
                 'name': 'Open Pull Requests'},
                {'x': repo['names'], 'y': repo['commits'], 'type': 'bar', 'name': 'Commits'},

            ],
            'layout': {
                'title': 'Activity for {}'.format(repo_name),
                'barmode': 'stack'
            }
        }
    )


app.layout = html.Div([
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # in milliseconds
        n_intervals=0
    ),
    html.Div(id='main_div')
]
)


@app.callback(Output('main_div', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_plots(n):
    return [
        make_stacked_bar_plot('MoravianCollege/capstone2020'),
        #make_stacked_bar_plot('MoravianCollege/cs334practice'),
        html.Div('Last Update: {};  Next Update: {}; API calls used this update: {};  Available API calls remaining {}'
                 .format(get_last_update_time(), get_next_update_time(), get_used_api_calls(),
                         get_remaining_api_calls()))
    ]


if __name__ == '__main__':
    app.run_server(debug=True)
