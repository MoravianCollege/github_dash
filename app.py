# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from github import Github
from dotenv import load_dotenv
import os

load_dotenv()
g = Github(os.getenv('GITHUB_TOKEN'))


def get_stats(repo_name):
    repo = g.get_repo(repo_name)

    names = []
    counts = []

    for stats_contrib in repo.get_stats_contributors():
        if stats_contrib.author.name is None:
            names.append(stats_contrib.author.login)
        else:
            names.append(stats_contrib.author.name)

        counts.append(stats_contrib.total)

        # print(stats_contrib.author.name, stats_contrib.author.login, stats_contrib.total)

    names.reverse()
    counts.reverse()

    return names, counts

mirr_names, mirr_counts = get_stats('MoravianCollege/mirrulations')
clash_names, clash_counts = get_stats('MoravianCollege/clashboard')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    dcc.Graph(
        id='mirrulations-graph',
        figure={
            'data': [
                {'x': mirr_names, 'y': mirr_counts, 'type': 'bar', 'name': 'mirrulations'},
            ],
            'layout': {
                'title': 'Total Commits to Mirrulations'
            }
        }
    ),

    dcc.Graph(
        id='clashboard-graph',
        figure={
            'data': [
                {'x': clash_names, 'y': clash_counts, 'type': 'bar', 'name': 'clashboard'},
            ],
            'layout': {
                'title': 'Total Commits to Clashboard'
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
