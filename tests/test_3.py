from collections.abc import Generator
from typing import Any

import pytest


def multiply(a: int, b: int) -> int:
    return a * b


@pytest.fixture
def sample_data() -> Generator[tuple[int], Any, None]:
    print("\n\nRUNNING BEFORE TEST! <-- setup goes here")
    yield (2, 5)
    print("\nRUNNING AFTER TEST! <-- cleanup goes here")


def test_multiply(sample_data):  # sample_data == (2, 6)
    a, b = sample_data

    result = multiply(a, b)
    print("\nASSERTING!")
    assert result == 10
