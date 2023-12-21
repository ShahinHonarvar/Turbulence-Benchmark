
def filter_chars(s):
    for c in s[78:87]:
        if ';' < c < 'r':
            s = s.replace(c, '')
    return s
