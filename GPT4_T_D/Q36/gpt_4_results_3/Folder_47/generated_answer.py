
def filter_chars(string):
    excluded_chars = {c for c in string[46:57] if 'F' < c < 'n'}
    return ''.join(c for c in string if c not in excluded_chars)
