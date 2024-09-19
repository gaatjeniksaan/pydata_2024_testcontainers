from collections.abc import Generator
from typing import Any

import pytest
import redis
from testcontainers.redis import RedisContainer

from pydata.my_cache import MyCache


@pytest.fixture(scope="function")
def redis_client() -> Generator[redis.Redis, Any, None]:
    with RedisContainer() as redis_container:
        # Additional setup goes here
        yield redis_container.get_client()


def test_write_to_cache_single(redis_client: redis.Redis) -> None:
    w = MyCache(redis_client=redis_client)
    key = "PyData2024"
    value = b"Amsterdam baby!!"
    w.write(key=key, value=value)

    assert w.get(key) == value
