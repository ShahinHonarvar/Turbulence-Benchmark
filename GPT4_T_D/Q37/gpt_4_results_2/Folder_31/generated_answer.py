
def filter_chars(s):
    for char in s[57:97]:
        if '<' <= char <= 'w':
            s = s.replace(char, '')
    return s
