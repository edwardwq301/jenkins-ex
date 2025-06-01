# your_homework_assignment/tests/test_basic.py
import pytest
from solution import add, subtract, multiply, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(0, 0) == 0


def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-5, 5) == 0


def test_subtract_positive_numbers():
    assert subtract(5, 2) == 3
    assert subtract(10, 10) == 0


def test_subtract_negative_numbers():
    assert subtract(2, 5) == -3
    assert subtract(-5, -2) == -3


def test_multiply_positive_numbers():
    assert multiply(2, 4) == 8
    assert multiply(0, 5) == 0


def test_multiply_negative_numbers():
    assert multiply(-2, 4) == -8
    assert multiply(-3, -3) == 9


def test_divide_positive_numbers():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_one():
    assert divide(5, 1) == 5.0


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)
