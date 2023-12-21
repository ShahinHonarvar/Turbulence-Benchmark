
def filter_chars(s):
    for c in s[476:948]:
        if 'b' < c < 'd':
            s = s.replace(c, '')
    return s
