
def filter_chars(s):
    for char in s[12:89]:
        if '&' <= char <= 'v':
            s = s.replace(char, '')
    return s
