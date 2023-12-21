
def filter_chars(string):
    return ''.join([c for c in string if not ('@' <= c <= 'T' and 10 <= string.index(c) <= 52)])
