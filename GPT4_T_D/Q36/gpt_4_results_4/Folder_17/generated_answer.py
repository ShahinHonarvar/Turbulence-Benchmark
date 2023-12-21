
def filter_chars(s):
    chars_to_remove = set([c for c in s[19:95] if 'K' < c < 'a'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
