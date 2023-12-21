
def filter_chars(string):
    return ''.join([c for c in string if not (13 <= string.index(c) <= 28 and 'c' <= c <= 'n')])
