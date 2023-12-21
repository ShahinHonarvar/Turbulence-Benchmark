
def filter_chars(string):
    chars_to_remove = set(string[42:68])
    return ''.join(c for c in string if c not in chars_to_remove or c <= 't' or c >= 'x')
