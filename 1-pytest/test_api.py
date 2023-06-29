import pytest
import requests
from unittest.mock import MagicMock
import api


@pytest.fixture
def mock_request_get():
    original_get = requests.get
    requests.get = MagicMock()
    yield
    requests.get = original_get


def test_get_todo(mock_request_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
    }
    requests.get.return_value = mock_response

    book = api_client.get_book_by_isbn(1)
    assert book == {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
    }
