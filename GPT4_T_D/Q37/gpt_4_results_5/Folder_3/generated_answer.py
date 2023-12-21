
def filter_chars(s):
    for char in s[37:57]:
        if '6' <= char <= '_':
            s = s.replace(char, '')
    return s
