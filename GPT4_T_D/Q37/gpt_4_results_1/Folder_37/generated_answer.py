
def filter_chars(s):
    chars = {c: None for c in s[17:64] if 'O' <= c <= '^'}
    return ''.join(c for c in s if c not in chars)
