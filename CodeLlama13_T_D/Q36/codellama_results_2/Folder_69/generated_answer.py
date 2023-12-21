
def filter_chars(s):
    for i in range(343, 665):
        c = s[i]
        if '%' < c < 'U':
            s = s.replace(c, '')
    return s
