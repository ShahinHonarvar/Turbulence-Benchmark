
def filter_chars(s):
    removed_chars = set([c for c in s[19:33] if 'f' <= c <= 'o'])
    return ''.join([c for c in s if c not in removed_chars])
