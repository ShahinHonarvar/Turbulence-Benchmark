
def filter_chars(s):
    for i in s[71:74]:
        if 'A' < i < 'U':
            s = s.replace(i, '')
    return s
