import pytest
from src.calculator.operations import addme, subtractme, multiplymen, divideme


@pytest.fixture
def setup():
    print("Setup before test")
    yield {"x": 3, "y": 5}
    print("Teardown after test")


def test_setup(setup):
    result = addme(setup["x"], setup["y"])
    assert result == 8


def test_add():
    assert addme(3, 5) == 8
    assert addme(0, 1) == 1
    assert addme(-3, -5) == -8
    assert addme(-4, 1) == -3


def test_subtract():
    assert subtractme(5, 3) == 2
    assert subtractme(-5, -3) == -2
    assert subtractme(2, 4) == -2


def test_multiply():
    assert multiplymen(3, 5) == 15
    assert multiplymen(-3, -5) == 15
    assert multiplymen(2, -4) == -8


def test_divide():
    assert divideme(10, 2) == 5
    assert divideme(-10, -2) == 5
    assert divideme(10, -2) == -5
    with pytest.raises(ValueError):
        divideme(0, 0)
