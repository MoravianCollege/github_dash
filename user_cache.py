

class UserCache:

    def __init__(self):
        self.the_cache = {}

    def is_cached(self, name):
        return name in self.the_cache

    def cache(self, login, name):
        self.the_cache[login] = name

    def get_value(self, login):
        return self.the_cache[login]

    def reset(self):
        self.the_cache = {}


user_cache = UserCache()
