
from user_stats import UserStats


def test_new_stats_are_all_zeros():

    u = UserStats('ben')

    assert u.get_name() is 'ben'
    assert u.get_commits() is 0
    assert u.get_open_pull_requests() is 0
    assert u.get_merges() is 0
    assert u.get_closed_pull_requests() is 0
    assert u.get_comments() is 0
    assert u.get_total() is 0

    assert u.as_dict() == {'name': 'ben', 'commits': 0, 'open_pull_requests': 0, 'merges': 0,
                           'comments': 0, 'closed_pull_requests': 0, 'total': 0}


def test_registering_values():
    u = UserStats('ben')

    u.register_commits(5)
    u.register_open_pull_requests(1)
    u.register_merges(2)
    u.register_comments(4)
    u.register_closed_pull_requests(3)

    assert u.get_name() is 'ben'
    assert u.get_commits() is 5
    assert u.get_open_pull_requests() is 1
    assert u.get_merges() is 2
    assert u.get_closed_pull_requests() is 3
    assert u.get_total() is 15

    assert u.as_dict() == {'name': 'ben', 'commits': 5, 'open_pull_requests': 1, 'merges': 2,
                           'comments': 4, 'closed_pull_requests': 3, 'total': 15}
