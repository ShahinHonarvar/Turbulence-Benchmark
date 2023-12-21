
def filter_chars(s):
    for i in range(421, 854):
        c = s[i]
        if 'D' < c < 'J':
            s = s.replace(c, '')
    return s
