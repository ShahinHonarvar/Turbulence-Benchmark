
def filter_chars(s):
    chars_to_remove = set([c for c in s[34:68] if 'W' <= c <= 'x'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
