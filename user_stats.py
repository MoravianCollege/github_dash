
class UserStats:

    def __init__(self, name):
        self.name = name
        self.commits = 0
        self.pull_requests = 0
        self.merges = 0

    def get_name(self):
        return self.name

    def get_commits(self):
        return self.commits

    def get_pull_requests(self):
        return self.pull_requests

    def get_merges(self):
        return self.merges

    def register_commits(self, num):
        self.commits += num

    def register_pull_requests(self, num):
        self.pull_requests += num

    def register_merges(self, num):
        self.merges += num
