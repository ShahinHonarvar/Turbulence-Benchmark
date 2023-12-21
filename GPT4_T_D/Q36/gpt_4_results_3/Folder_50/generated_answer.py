
def filter_chars(s):
    for c in s[62:88]:
        if '%' < c < 'q':
            s = s.replace(c, '')
    return s
