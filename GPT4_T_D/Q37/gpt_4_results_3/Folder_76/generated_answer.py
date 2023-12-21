
def filter_chars(s):
    remove_chars = set([c for c in s[379:899] if 'M' <= c <= 'v'])
    s = ''.join([c for c in s if c not in remove_chars])
    return s
