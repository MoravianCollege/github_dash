
class UserStats:

    def __init__(self, name):
        self.name = name
        self.commits = 0
        self.open_pull_requests = 0
        self.merges = 0
        self.comments = 0
        self.closed_pull_requests = 0

    def get_name(self):
        return self.name

    def get_commits(self):
        return self.commits

    def get_open_pull_requests(self):
        return self.open_pull_requests

    def get_closed_pull_requests(self):
        return self.closed_pull_requests

    def get_merges(self):
        return self.merges

    def get_comments(self):
        return self.comments

    def get_total(self):
        return self.commits + self.open_pull_requests + self.closed_pull_requests + self.merges + self.comments

    def register_commits(self, num):
        self.commits += num

    def register_open_pull_requests(self, num):
        self.open_pull_requests += num

    def register_closed_pull_requests(self, num):
        self.closed_pull_requests += num

    def register_comments(self, num):
        self.comments += num

    def register_merges(self, num):
        self.merges += num

    def as_dict(self):
        return {'name': self.name, 'commits': self.commits, 'open_pull_requests':self.open_pull_requests,
                'closed_pull_requests': self.closed_pull_requests, 'merges': self.merges, 'comments': self.comments,
                'total': self.get_total()}
