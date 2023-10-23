import pytest


def test_check_str_len():
    phrase = input('Print string for checking: ')
    assert len(phrase) <= 15, 'Phrase length is more than 15!'
