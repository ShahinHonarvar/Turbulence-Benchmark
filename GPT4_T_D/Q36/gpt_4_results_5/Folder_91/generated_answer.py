
def filter_chars(s):
    for c in s[1:3]:
        if '$' < c < '?':
            s = s.replace(c, '')
    return s
