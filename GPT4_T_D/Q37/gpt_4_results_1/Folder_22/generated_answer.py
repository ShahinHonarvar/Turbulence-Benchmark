
def filter_chars(s):
    target_chars = set(filter(lambda c: '7' <= c <= 'k', s[33:71]))
    return ''.join(c for c in s if c not in target_chars)
