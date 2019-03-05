from repo_users import RepoUsers
from github import Github
from dotenv import load_dotenv
from user_cache import user_cache

import os


def make_user_stats(repo_name):

    load_dotenv()
    g = Github(os.getenv('GITHUB_TOKEN'))

    repo_users = RepoUsers(repo_name)
    repo = g.get_repo(repo_name)

    for stats_contrib in repo.get_stats_contributors():
        repo_users.register_commits(get_name(stats_contrib.author), stats_contrib.total)

    for pr in repo.get_pulls(state='closed'):
        repo_users.register_closed_pull_requests(get_name(pr.user), 1)
        if pr.merged_by is not None:
            repo_users.register_merges(get_name(pr.merged_by), 1)

        # See comment in app.py
        for comment in pr.get_comments():
            repo_users.register_comments(get_name(comment.user), 1)

    # state = open by default
    for pr in repo.get_pulls():
        repo_users.register_open_pull_requests(get_name(pr.user), 1)

        # See previous loop
        for comment in pr.get_comments():
            repo_users.register_comments(get_name(comment.user), 1)

    return repo_users


def get_name(named_user):
    if not user_cache.is_cached(named_user.login):
        if named_user.name is None:
            user_cache.cache(named_user.login, named_user.login)
        user_cache.cache(named_user.login, named_user.name)

    return user_cache.get_value(named_user.login)
