import pytest
import redis

from pydata.my_cache import MyCache


@pytest.mark.parametrize("value", ([bytes(x) for x in range(100)]))
def test_write_to_cache_parametrized(value: str, redis_client: redis.Redis) -> None:
    w = MyCache(redis_client=redis_client)
    key = "PyData2024"
    w.write(key=key, value=value)

    assert w.get(key) == value
