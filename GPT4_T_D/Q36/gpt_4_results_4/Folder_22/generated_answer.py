
def filter_chars(s):
    for i in s[56:84]:
        if ';' < i < 'z':
            s = s.replace(i, '')
    return s
