
def filter_chars(s):
    for c in s[19:64]:
        if '3' < c < 'B':
            s = s.replace(c, '')
    return s
