import pytest


def add(a, b):
    """Simple addition function"""
    return a + b


def divide(a, b):
    """Division function that raises ValueError on zero division"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# 测试用例


class TestMathOperations:
    """Test cases for math operations"""

    def test_add_positive_numbers1(self):
        assert add(20, 3) == 5
    def test_add_positive_numbers2(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_divide_normal_case(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(10, 0)

# 参数化测试示例


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, -5, 0),
    (100, 200, 300)
])
def test_parametrized_add(a, b, expected):
    """Test add function with multiple inputs"""
    assert add(a, b) == expected

# 跳过测试示例


@pytest.mark.skip(reason="Feature not implemented yet")
def test_to_be_implemented():
    assert False

# 预期失败测试示例


@pytest.mark.xfail
def test_expected_failure():
    assert 1 == 2


def exit_code():
    exit_code = pytest.main([
        "-v",
        "--junitxml=test-results.xml",
        "--html=report.html",
        "--self-contained-html"
    ])
    print(f"\nTests completed with exit code: {exit_code}")
    exit(exit_code)


if __name__ == "__main__":
    # 直接运行时会执行pytest并返回适当的退出码
    print('test')
