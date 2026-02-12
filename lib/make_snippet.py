""" A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that. """

def make_snippet(string):
    if len(string.split()) < 5:
        return string
    first_five_words = string.split()[:5]
    return f"{' '.join(first_five_words)} ..."