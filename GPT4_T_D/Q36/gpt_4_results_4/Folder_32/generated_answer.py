
def filter_chars(s):
    for c in s[41:63]:
        if '7' < c < 'H':
            s = s.replace(c, '')
    return s
