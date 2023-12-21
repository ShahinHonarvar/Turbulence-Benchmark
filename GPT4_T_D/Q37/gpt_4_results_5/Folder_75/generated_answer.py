
def filter_chars(s):
    to_remove = set(c for i, c in enumerate(s) if 34 <= i <= 67 and 'W' <= c <= 'x')
    return ''.join(c for c in s if c not in to_remove)
