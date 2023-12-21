
def filter_chars(s):
    for c in s[46:86]:
        if '-' <= c <= 'X':
            s = s.replace(c, '')
    return s
