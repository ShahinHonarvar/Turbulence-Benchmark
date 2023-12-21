
def filter_chars(s):
    for c in set(s[24:83]):
        if '5' <= c <= '<':
            s = s.replace(c, '')
    return s
