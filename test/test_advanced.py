import pytest
from solution import add, subtract, multiply, divide


@pytest.mark.parametrize("a, b, expected", [
    (0.1, 0.2, 0.3),
    (1.5, -2.5, -1.0),
    (-0.1, -0.2, -0.3)
])
def test_add_float_numbers(a, b, expected):
    # Use pytest.approx for float comparisons
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (3.14, 1.0, 2.14),
    (-0.5, 0.5, -1.0),
    (10.0, 3.0, 7.0)
])
def test_subtract_float_numbers(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (2.5, 2.0, 5.0),
    (-1.5, 3.0, -4.5),
    (0.0, 5.0, 0.0)
])
def test_multiply_float_numbers(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (1.0, 3.0, 1/3),
    (100.0, 7.0, 100/7),
    (5.0, 0.5, 10.0)
])
def test_divide_float_numbers(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_large_numbers():
    assert divide(1_000_000, 3) == pytest.approx(333333.3333333333)


def test_add_mixed_types_raises_error():
    # Pytest's raises context manager is similar to unittest's
    with pytest.raises(TypeError):
        add(5, "hello")


def test_performance_with_large_numbers():
    # This isn't a true performance test, but ensures correctness for large inputs
    result = add(1_000_000_000, 2_000_000_000)
    assert result == 3_000_000_000
