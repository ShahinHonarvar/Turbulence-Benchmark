
def filter_chars(s):
    for i in s[78:87]:
        if ';' < i < 'r':
            s = s.replace(i, '')
    return s
