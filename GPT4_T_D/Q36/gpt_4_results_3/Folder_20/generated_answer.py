
def filter_chars(s):
    for c in s[14:40]:
        if c > ':' and c < 'C':
            s = s.replace(c, '')
    return s
