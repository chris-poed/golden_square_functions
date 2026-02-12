# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def reading_time():
    """
    Calculates reading time based on 200 words per minute

    Parameters: 
        text: a string of text containing words and numbers

    Returns:
        a string containing hours and minutes

    Side effects:
        This function doesn't print anything or have any other side-effects
    """
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a string of 200 words
It returns a reading time of 1 minute
"""

reading_time('...200...') => 'Estimated reading time is 1 minute'

"""
Given a string of 400 words
It returns a reading time of 2 minute
"""

reading_time('...400...') => 'Estimated reading time is 2 minutes'

"""
Given a string of 100,000 words
It returns a reading time of 8 hours 20 minutes
"""

reading_time('...100000...') => 'Estimated reading time is 8 hours and 20 minutes'

"""
Given a string of less than 200 words
It returns a reading time of less than 1 minute
"""
reading_time('...50...') => 'Estimated reading time is less than a minute'

"""
Given a data type other than string
It returns an error
"""
reading_time(integer) => 'Please provide some text'

```

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
