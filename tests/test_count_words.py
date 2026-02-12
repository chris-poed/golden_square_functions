import pytest
from lib.count_words import *

# A function called count_words that takes a string as an argument and returns the number of words in that string.

def test_returns_0_when_passed_an_empty_string():
    assert count_words('') == 0

def test_returns_1_when_passed_1_word():
    assert count_words('hello') == 1

def test_returns_5_when_passed_5_words():
    assert count_words('hello my name is chris') == 5
