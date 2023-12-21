
def filter_chars(s):
    for c in s[56:84]:
        if ';' < c < 'z':
            s = s.replace(c, '')
    return s
