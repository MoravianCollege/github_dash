
from user_stats import UserStats


def test_new_stats_are_all_zeros():

    u = UserStats('ben')

    assert u.get_name() is 'ben'
    assert u.get_commits() is 0
    assert u.get_pull_requests() is 0
    assert u.get_merges() is 0


def test_registering_values():
    u = UserStats('ben')

    u.register_commits(5)
    u.register_pull_requests(1)
    u.register_merges(2)

    assert u.get_name() is 'ben'
    assert u.get_commits() is 5
    assert u.get_pull_requests() is 1
    assert u.get_merges() is 2
