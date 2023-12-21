
def filter_chars(s):
    chars_to_remove = set([c for c in s[41:65] if 'K' <= c <= ']'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
