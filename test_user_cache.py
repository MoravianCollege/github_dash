
from user_cache import user_cache


def test_missing_user():
    assert user_cache.is_cached('ben') is False


def test_name_is_remembered():
    user_cache.reset()
    assert user_cache.is_cached('bjcoleman') is False
    user_cache.cache('bjcoleman', 'Ben Coleman')
    assert user_cache.is_cached('bjcoleman') is True
    assert user_cache.get_value('bjcoleman') is 'Ben Coleman'
