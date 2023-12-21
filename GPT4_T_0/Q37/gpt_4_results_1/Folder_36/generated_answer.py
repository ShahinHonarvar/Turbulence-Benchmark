
def filter_chars(s):
    chars_to_remove = set([c for c in s[259:503] if ',' <= c <= '3'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
