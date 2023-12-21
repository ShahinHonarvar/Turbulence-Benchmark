
def filter_chars(s):
    chars_to_remove = set([c for c in s[515:539] if '+' <= c <= '}'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
