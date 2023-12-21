
def filter_chars(s):
    chars_to_remove = set([c for c in s[38:100] if 'A' <= c <= 'Q'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
