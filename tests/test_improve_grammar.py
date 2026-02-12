import pytest
from lib.improve_grammar import check_grammar

def test_check_sentence_with_correct_grammar():
    assert check_grammar('This is a sentence with correct grammar.') == 'Yes this has correct grammar.'

def test_check_sentence_starting_with_lowercase():
    assert check_grammar('this sentence does not have correct grammar!') == 'No, this is incorrect grammar.'

def test_check_sentence_ending_with_punctuation():
    assert check_grammar('This sentence does not have correct grammar') == 'No, this is incorrect grammar.'