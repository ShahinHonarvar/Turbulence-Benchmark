
def filter_chars(s):
    for i in s[64:89]:
        if '*' < i < 'w':
            s = s.replace(i, '')
    return s
