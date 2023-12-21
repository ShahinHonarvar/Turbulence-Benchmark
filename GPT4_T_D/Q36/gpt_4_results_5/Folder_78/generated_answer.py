
def filter_chars(s):
    for c in s[30:33]:
        if '%' < c < 'a':
            s = s.replace(c, '')
    return s
