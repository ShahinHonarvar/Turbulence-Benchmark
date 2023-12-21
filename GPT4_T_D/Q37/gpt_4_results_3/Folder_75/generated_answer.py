
def filter_chars(str):
    chars_to_remove = set([c for i, c in enumerate(str) if 34 <= i <= 67 and 'W' <= c <= 'x'])
    return ''.join([c for c in str if c not in chars_to_remove])
