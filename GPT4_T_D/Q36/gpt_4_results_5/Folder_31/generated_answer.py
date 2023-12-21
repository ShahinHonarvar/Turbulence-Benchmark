
def filter_chars(s):
    for c in s[15:75]:
        if '9' < c < 'K':
            s = s.replace(c, '')
    return s
