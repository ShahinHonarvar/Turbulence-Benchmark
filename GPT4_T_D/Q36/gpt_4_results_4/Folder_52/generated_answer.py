
def filter_chars(s):
    for c in s[50:56]:
        if 'I' < c < 'a':
            s = s.replace(c, '')
    return s
