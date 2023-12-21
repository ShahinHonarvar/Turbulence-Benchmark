def filter_chars(s):
    return ''.join(c for c in s if c not in ';b' and 27 <= ord(c) <= 29)
