
def filter_chars(s):
    for c in s[44:69]:
        if 'B' < c < 'r':
            s = s.replace(c, '')
    return s
