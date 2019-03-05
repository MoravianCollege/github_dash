
import os
from github import Github
from dotenv import load_dotenv
from user_cache import user_cache
from github_stats import make_user_stats

load_dotenv()
g = Github(os.getenv('GITHUB_TOKEN'))


def count(func, *args):
    before = g.rate_limiting[0]
    ret = func(*args)
    g.get_rate_limit()
    after = g.rate_limiting[0]
    print(func.__name__, before - after)
    return ret


def get_name(named_user):
    if not user_cache.is_cached(named_user.login):
        if named_user.name is None:
            user_cache.cache(named_user.login, named_user.login)
        user_cache.cache(named_user.login, named_user.name)

    return user_cache.get_value(named_user.login)


def go():
    repo = g.get_repo('MoravianCollege/clashboard')
    for pr in repo.get_pulls(state='all'):
        print(get_name(pr.user))


#count(go)

count(make_user_stats, 'MoravianCollege/clashboard')
count(make_user_stats, 'MoravianCollege/mirrulations')