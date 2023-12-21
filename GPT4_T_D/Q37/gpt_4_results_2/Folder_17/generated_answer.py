
def filter_chars(s):
    banned_chars = {c for c in s[27:30] if ';' <= c <= 'b'}
    return ''.join(c for c in s if c not in banned_chars)
