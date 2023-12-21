
def filter_chars(s):
    for c in s[34:36]:
        if '>' < c < 'A':
            s = s.replace(c, '')
    return s
