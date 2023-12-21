
def filter_chars(s):
    for c in s[673:709]:
        if 'X' < c < '}':
            s = s.replace(c, '')
    return s
