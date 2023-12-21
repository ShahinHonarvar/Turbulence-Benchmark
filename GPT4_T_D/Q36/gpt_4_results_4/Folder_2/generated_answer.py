
def filter_chars(s):
    for c in s[422:854]:
        if 'D' < c < 'J':
            s = s.replace(c, '')
    return s
