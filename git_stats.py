
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

g = Github(os.getenv('GITHUB_TOKEN'))

def print_stats(repo_name):

    repo = g.get_repo(repo_name)

    print(repo.name)

    names = []
    counts = []

    for stats_contrib in repo.get_stats_contributors():
        names.append('{} ({})'.format(stats_contrib.author.name, stats_contrib.author.login))
        counts.append(stats_contrib.total)

        print(stats_contrib.author.name, stats_contrib.author.login, stats_contrib.total)

    return names, counts

print_stats('MoravianCollege/mirrulations')
print_stats('MoravianCollege/clashboard')