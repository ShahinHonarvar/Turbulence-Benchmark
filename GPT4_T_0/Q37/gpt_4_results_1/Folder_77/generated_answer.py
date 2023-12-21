
def filter_chars(s):
    chars_to_remove = set([c for c in s[384:412] if '/' <= c <= '8'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
