
def filter_chars(s):
    for c in s[24:45]:
        if '3' < c < 'I':
            s = s.replace(c, '')
    return s
