
def filter_chars(s):
    for c in s[64:89]:
        if '*' < c < 'w':
            s = s.replace(c, '')
    return s
