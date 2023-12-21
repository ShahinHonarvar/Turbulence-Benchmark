
def filter_chars(s):
    chars_to_remove = set([c for c in s[35:99] if 'A' <= c <= 'b'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
