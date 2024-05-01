import pytest
from calculator.operations import add, subtract, multiply, divide


@pytest.fixture
def setup():
    print("Setup before test")
    yield {"x": 3, "y": 5}
    print("Teardown after test")


def test_setup(setup):
    result = add(setup["x"], setup["y"])
    assert result == 8


def test_add():
    assert add(3, 5) == 8
    assert add(0, 1) == 1
    assert add(-3, -5) == -8
    assert add(-4, 1) == -3


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, -3) == -2
    assert subtract(2, 4) == -2


def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(-3, -5) == 15
    assert multiply(2, -4) == -8


def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, -2) == 5
    assert divide(10, -2) == -5
    with pytest.raises(ValueError):
        divide(0, 0)
