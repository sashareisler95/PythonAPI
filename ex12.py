import pytest
import requests


def test_check_cookie():
    response = requests.get('https://playground.learnqa.ru/api/homework_header', verify=False)
    headers_value = response.headers
    assert len(headers_value) != 0, 'No headers in response!'
    assert 'x-secret-homework-header' in headers_value, 'There is no secret header in the response!'
