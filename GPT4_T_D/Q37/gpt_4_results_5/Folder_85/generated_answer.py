
def filter_chars(s):
    chars_to_remove = {c for i, c in enumerate(s) if 28 <= i <= 65 and 'O' <= c <= 'd'}
    return ''.join(c for c in s if c not in chars_to_remove)
