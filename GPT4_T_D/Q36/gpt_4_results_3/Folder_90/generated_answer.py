
def filter_chars(string):
    chars = set(c for c in string[345:874] if 'f' < c < '~')
    return ''.join(c for c in string if c not in chars)
