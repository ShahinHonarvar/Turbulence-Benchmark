
def filter_chars(s):
    chars_to_remove = set([c for c in s[54:63] if ')' <= c <= '9'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
