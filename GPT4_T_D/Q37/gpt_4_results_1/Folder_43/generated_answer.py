
def filter_chars(s):
    to_remove = set([c for c in s[15:56] if 'W' <= c <= '{'])
    return ''.join(c for c in s if c not in to_remove)
