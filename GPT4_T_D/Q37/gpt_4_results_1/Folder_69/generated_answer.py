
def filter_chars(s):
    to_remove = set([c for c in s[114:640] if c >= '!' and c <= 'x'])
    return ''.join(c for c in s if c not in to_remove)
