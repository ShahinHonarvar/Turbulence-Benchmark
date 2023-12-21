
def filter_chars(s):
    for c in s[36:60]:
        if '!' < c < 'B':
            s = s.replace(c, '')
    return s
