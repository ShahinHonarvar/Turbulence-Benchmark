
def filter_chars(s):
    for i in s[344:665]:
        if '%' < i < 'U':
            s = s.replace(i, '')
    return s
