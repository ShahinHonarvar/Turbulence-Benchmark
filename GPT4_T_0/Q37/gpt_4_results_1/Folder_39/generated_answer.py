
def filter_chars(s):
    chars_to_remove = set([c for c in s[52:82] if 'A' <= c <= 'U'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
