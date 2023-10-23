import pytest
import requests


def test_check_cookie():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie', verify=False)
    cookie_value = response.cookies.values()
    cookie_value = ''.join(cookie_value)
    cookie_name = response.cookies.keys()
    cookie_name = ''.join(cookie_name)
    assert cookie_name == 'HomeWork' and cookie_value == 'hw_value', 'Cookies is not correct!'
