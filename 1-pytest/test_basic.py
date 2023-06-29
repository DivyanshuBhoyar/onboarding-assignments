import basics
import pytest


def test_multiply(multiply_data):
    assert basics.multiply(2, 3) == 6
    assert basics.multiply(89, 0) == 0
    a, b, res = multiply_data
    assert basics.multiply(a, b) == res


@pytest.mark.parametrize("a, b, res, expected_exception", [
    (10, 2, 5, None), (100, 4, 25, None), (2, 2, 1, None), (9, 0, None, ValueError)
])
def test_divide(a, b, res, expected_exception):
    if expected_exception:
        with pytest.raises(expected_exception):
            basics.divide(a, b)
    else:
        assert basics.divide(a, b) == res
