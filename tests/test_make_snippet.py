import pytest
from lib.make_snippet import *

def test_returns_full_string():
    assert make_snippet('hello') == 'hello'

def test_returns_truncated_string_when_length_greater_than_5_words():
    assert make_snippet('well hello there my name is chris ') == 'well hello there my name ...'

def test_returns_empty_string_when_passed_empty_string():
    assert make_snippet('') == ''