
def filter_chars(s):
    to_remove = set(c for c in s[51:97] if 'X' <= c <= 'p')
    return ''.join(c for c in s if c not in to_remove)
