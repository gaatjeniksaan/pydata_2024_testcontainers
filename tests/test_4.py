from testcontainers.redis import RedisContainer

from pydata.my_cache import MyCache


def test_write_to_cache_single_no_fixture() -> None:
    c = RedisContainer()
    c.start()
    redis_client = c.get_client()

    w = MyCache(redis_client=redis_client)
    key = "PyData2024"
    value = b"Amsterdam baby!!"
    w.write(key=key, value=value)

    assert w.get(key) == value
    c.stop()
