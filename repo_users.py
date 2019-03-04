
from user_stats import UserStats


class RepoUsers:

    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.users = {}

    def register_commits(self, name, num):
        self.add_if_missing(name)
        self.users[name].register_commits(num)

    def register_open_pull_requests(self, name, num):
        self.add_if_missing(name)
        self.users[name].register_open_pull_requests(num)

    def register_closed_pull_requests(self, name, num):
        self.add_if_missing(name)
        self.users[name].register_closed_pull_requests(num)

    def register_merges(self, name, num):
        self.add_if_missing(name)
        self.users[name].register_merges(num)

    def register_comments(self, name, num):
        self.add_if_missing(name)
        self.users[name].register_comments(num)

    def get_repo_name(self):
        return self.repo_name

    def get_dict_of_arrays(self):
        ret = [user.as_dict() for user in self.users.values()]
        sorted_users = sorted(ret, key=lambda key: key['total'], reverse=True)

        names = [user['name'] for user in sorted_users]
        commits = [user['commits'] for user in sorted_users]
        open_pull_requests = [user['open_pull_requests'] for user in sorted_users]
        closed_pull_requests = [user['closed_pull_requests'] for user in sorted_users]
        merges = [user['merges'] for user in sorted_users]
        comments = [user['comments'] for user in sorted_users]

        return {'names': names, 'commits': commits, 'open_pull_requests': open_pull_requests,
                'closed_pull_requests': closed_pull_requests, 'merges': merges, 'comments': comments}

    def add_if_missing(self, name):
        if name not in self.users:
            self.users[name] = UserStats(name)
