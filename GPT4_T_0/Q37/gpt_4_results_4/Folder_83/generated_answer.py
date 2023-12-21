
def filter_chars(s):
    chars_to_remove = set([c for c in s[29:80] if 'K' <= c <= 'z'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
