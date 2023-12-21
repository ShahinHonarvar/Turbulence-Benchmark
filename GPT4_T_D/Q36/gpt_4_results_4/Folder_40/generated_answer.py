
def filter_chars(s):
    char_range = set(s[2:7])
    for c in char_range:
        if '-' < c < 'L':
            s = s.replace(c, '')
    return s
