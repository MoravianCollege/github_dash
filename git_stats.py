
import os
from github import Github
from dotenv import load_dotenv
from repo_users import RepoUsers

load_dotenv()

g = Github(os.getenv('GITHUB_TOKEN'))


def get_name(named_user):
    if named_user.name is None:
        return named_user.login
    return named_user.name


repo = g.get_repo('MoravianCollege/clashboard')


for pr in repo.get_pulls(state='all'):
    for comment in pr.get_comments():
        print('comment:', comment, get_name(comment.user))

    for issue_comment in pr.get_issue_comments():
        print('issue comment:', issue_comment, get_name(issue_comment.user))
