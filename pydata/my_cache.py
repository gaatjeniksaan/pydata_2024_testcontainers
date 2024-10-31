import typing
import redis


class MyCache:
    """MyCache is a flimsy wrapper around Redis :')."""

    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    def write(self, key: str, value: bytes | str) -> None:
        self.redis_client.set(key, value)

    def get(self, key: str) -> typing.Any:
        return self.redis_client.get(key)
