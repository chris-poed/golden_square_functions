# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammar(text):
    """Checks that some text starts with a capital letter and ends with a . or !

    Parameters:
        text: a string containing words (e.g. "This is a sentence.")

    Returns: 
        None

    Side effects: (state any side effects)
        if True, prints 'Yes, this has correct grammar.'
        if False, prints 'No, this is incorrect grammar.'
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string starting with a capital letter and ending in . or !
Prints 'Yes, this has correct grammar'
"""
check_grammar('This is a sentence with correct grammar.') => 'Yes this has correct grammar.'

"""
Given a string starting with lowercase letter and ending in . or !
Prints 'No, this is incorrect grammar.'
"""
check_grammar('this sentence does not have correct grammar!') => 'No, this is incorrect grammar.'

"""
Given a string starting with a capital letter but not ending with . or !
Prints 'No, this is incorrect grammar.'
"""
check_grammar('This sentence does not have correct grammar') => 'No, this is incorrect grammar.'


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
