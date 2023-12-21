
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 515 or i > 538 or not ('+' <= c <= '}'))
