def filter_chars(s):
    return ''.join(c for c in s if c not in range(48, 75, 1) and c not in '6789_')
