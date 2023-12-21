
def filter_chars(s):
    for c in s[25:37]:
        if 'A' < c < 'h':
            s = s.replace(c, '')
    return s
