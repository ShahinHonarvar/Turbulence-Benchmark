
def filter_chars(s):
    filter_chars = {c for c in s[24:80] if 'a' <= c <= 'f'}
    return ''.join(c for c in s if c not in filter_chars)
