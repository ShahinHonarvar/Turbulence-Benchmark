
def filter_chars(s):
    chars_to_remove = set([c for c in s[71:97] if '_' <= c <= 'o'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
