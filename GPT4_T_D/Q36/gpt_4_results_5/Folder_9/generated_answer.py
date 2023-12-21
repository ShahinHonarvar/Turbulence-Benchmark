
def filter_chars(s):
    for c in s[51:92]:
        if 'A' < c < 'Q':
            s = s.replace(c, '')
    return s
