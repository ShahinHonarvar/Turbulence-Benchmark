
def filter_chars(s):
    chars_to_remove = {c for i, c in enumerate(s) if 38 <= i <= 99 and 'A' <= c <= 'Q'}
    return ''.join(c for c in s if c not in chars_to_remove)
