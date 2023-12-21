def filter_chars(s):
    return ''.join(c for c in s if c not in set(c for c in range(27, 76) if c in 'ABCDEFGHI'))
