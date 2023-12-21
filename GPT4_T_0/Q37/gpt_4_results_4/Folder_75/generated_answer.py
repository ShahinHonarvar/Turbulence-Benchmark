
def filter_chars(s):
    chars_to_remove = set([c for c in s[34:68] if 'W' <= c <= 'x'])
    return ''.join([c for c in s if c not in chars_to_remove])
