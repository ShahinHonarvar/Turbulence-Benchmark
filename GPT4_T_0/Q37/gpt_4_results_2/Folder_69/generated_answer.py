
def filter_chars(s):
    chars_to_remove = set([c for c in s[114:640] if '!' <= c <= 'x'])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s
