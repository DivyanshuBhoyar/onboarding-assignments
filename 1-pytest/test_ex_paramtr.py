import ex_paramtr
import pytest

@pytest.mark.parametrize("username,expected", [
    ("user1", True),
    ("user3", False),
])
def test_is_registered(username, expected):
    assert ex_paramtr.is_registered(username) == expected

@pytest.mark.parametrize("username,password,expected", [
    ("user1", "password1", True),
    ("user1", "wrong_password", False),
    ("user3", "password3", False),
])
def test_authenticate(username, password, expected):
    assert ex_paramtr.authenticate(username, password) == expected