import pytest


@pytest.fixture
def test_add_numbers() -> list:
    numbers = [1, 2]
    result = sum(numbers)
    return numbers, result
