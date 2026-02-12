def check_grammar(text):
    first_letter_is_capital = text[0].isupper()
    ends_with_punctuation = text[-1] == '.' or text[-1] == '!'
    if first_letter_is_capital and ends_with_punctuation:
        return 'Yes this has correct grammar.'
    return 'No, this is incorrect grammar.'