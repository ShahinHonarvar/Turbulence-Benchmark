
def filter_chars(s):
    for c in s[43:68]:
        if 't' < c < 'x':
            s = s.replace(c, '')
    return s
