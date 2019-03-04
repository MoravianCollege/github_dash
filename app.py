# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from github_stats import make_user_stats

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def make_stacked_bar_plot(repo_name):
    repo = make_user_stats(repo_name).get_dict_of_arrays()

    return {
        'data': [
            # Comments ommited for not for performance reasons.  This nearly
            # doubles the number of API calls.  Also commented out out in github_stats.py
            #{'x': repo['names'], 'y': repo['comments'], 'type': 'bar', 'name': 'Comments'},
            {'x': repo['names'], 'y': repo['merges'], 'type': 'bar', 'name': 'Merges'},
            {'x': repo['names'], 'y': repo['closed_pull_requests'], 'type': 'bar',
             'name': 'Closed Pull Requests'},
            {'x': repo['names'], 'y': repo['open_pull_requests'], 'type': 'bar',
             'name': 'Open Pull Requests'},
            {'x': repo['names'], 'y': repo['commits'], 'type': 'bar', 'name': 'Commits'},

        ],
        'layout': {
            'title': '{} Activity'.format(repo_name),
            'barmode': 'stack'
        }
    }


app.layout = html.Div(children=[

    dcc.Graph(
        id='clashboard-graph',
        figure=make_stacked_bar_plot('MoravianCollege/clashboard')
    ),

    dcc.Graph(
        id='mirrulations-graph',
        figure=make_stacked_bar_plot('MoravianCollege/mirrulations')
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
