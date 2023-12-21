def filter_chars(s):
    return ''.join(c for c in s if c not in '-v' and c not in s[221:419])
