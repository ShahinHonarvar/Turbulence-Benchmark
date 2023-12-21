
def filter_chars(s):
    chars_to_remove = set(c for i, c in enumerate(s) if 379 <= i <= 898 and 'M' <= c <= 'v')
    return ''.join(c for c in s if c not in chars_to_remove)
