from collections.abc import Generator
from typing import Any

import pytest
import redis
from testcontainers.redis import RedisContainer

from pydata.my_cache import MyCache


@pytest.fixture(scope="session")
def redis_client_session() -> Generator[redis.Redis, Any, None]:
    with RedisContainer() as redis_container:
        # Additional setup goes here
        yield redis_container.get_client()


@pytest.mark.parametrize(
        "value",
        ([bytes(x) for x in range(12)]),
        ids=[f"run {x}" for x in range(12)],
    )
def test_write_to_cache_parametrized(value: str, redis_client_session: redis.Redis) -> None:
    w = MyCache(redis_client=redis_client_session)
    key = "Data Rocks 8"
    w.write(key=key, value=value)

    assert w.get(key) == value
