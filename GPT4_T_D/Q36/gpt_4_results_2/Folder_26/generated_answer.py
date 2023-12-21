
def filter_chars(s):
    for c in s[44:83]:
        if ':' < c < 'Q':
            s = s.replace(c, '')
    return s
