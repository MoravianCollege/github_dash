
from repo_users import RepoUsers


def test_new_instance_empty():
    ru = RepoUsers('repo')
    assert ru.get_dict_of_arrays() == {'names': [], 'commits': [], 'open_pull_requests': [],
                                       'closed_pull_requests': [], 'merges': [], 'comments': []}


def test_dict_of_arrays_view():
    ru = RepoUsers('repo')

    ru.register_commits('Ben', 5)
    ru.register_commits('Lauri', 10)
    ru.register_commits('Seth', 4)
    ru.register_commits('Sharon', 7)

    ru.register_open_pull_requests('Ben', 13)
    ru.register_open_pull_requests('Lauri', 10)
    ru.register_open_pull_requests('Seth', 4)
    ru.register_open_pull_requests('Sharon', 12)

    ru.register_closed_pull_requests('Ben', 4)
    ru.register_closed_pull_requests('Lauri', 2)
    ru.register_closed_pull_requests('Seth', 5)
    ru.register_closed_pull_requests('Sharon', 1)

    ru.register_merges('Ben', 3)
    ru.register_merges('Lauri', 42)
    ru.register_merges('Seth', 2)
    ru.register_merges('Sharon', 20)

    ru.register_comments('Ben', 2)
    ru.register_comments('Lauri', 4)
    ru.register_comments('Seth', 1)
    ru.register_comments('Sharon', 3)

    names = ['Lauri', 'Sharon', 'Ben', 'Seth']
    commits = [10, 7, 5, 4]
    open_pulls = [10, 12, 13, 4]
    closed_pulls = [2, 1, 4, 5]
    merges = [42, 20, 3, 2]
    comments = [4, 3, 2, 1]

    ret = ru.get_dict_of_arrays()

    assert ret['names'] == names
    assert ret['commits'] == commits
    assert ret['open_pull_requests'] == open_pulls
    assert ret['closed_pull_requests'] == closed_pulls
    assert ret['merges'] == merges
    assert ret['comments'] == comments
