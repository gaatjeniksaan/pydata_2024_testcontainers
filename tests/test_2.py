from unittest import mock

from pydata.my_cache import MyCache


def test_write_to_cache_with_mock_java() -> None:
    key = "Data Rocks 8"
    value = b"Love you!"

    mock_redis = mock.Mock()
    mock_redis.get.return_value = value

    w = MyCache(redis_client=mock_redis)
    w.write(key=key, value=value)

    # No test should ever pass this...
    assert w.get("I <3 Java") == value
