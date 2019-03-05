from redis import Redis
from github_collect.github_stats import make_user_stats
import time
from github import Github
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
r = Redis()

repos = ['MoravianCollege/mirrulations', 'MoravianCollege/clashboard']
DELAY_MINUTES = 5


def make_hour_minute_time_string(timestamp):
    return timestamp.strftime('%-I:%M')


def go():

    g = Github(os.getenv('GITHUB_TOKEN'))

    while True:

        before = g.rate_limiting[0]

        try:
            for repo_name in repos:

                stats = make_user_stats(repo_name)

                r.set(repo_name, str(stats.get_dict_of_arrays()))

            last_update = datetime.datetime.now()
            next_update = datetime.datetime.now() + datetime.timedelta(minutes=DELAY_MINUTES)

            r.set('last_update', make_hour_minute_time_string(last_update))
            r.set('next_update', make_hour_minute_time_string(next_update))
        except:
            pass

        g.get_rate_limit()
        after = g.rate_limiting[0]
        used = before - after

        r.set('used', used)
        r.set('remaining', after)

        time.sleep(60 * DELAY_MINUTES)


if __name__ == '__main__':
    go()
