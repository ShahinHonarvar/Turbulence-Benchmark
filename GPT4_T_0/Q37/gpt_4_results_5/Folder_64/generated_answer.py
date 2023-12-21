
def filter_chars(s):
    chars_to_remove = set([c for c in s[1:8] if 'L' <= c <= 'a'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
