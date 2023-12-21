
def filter_chars(s):
    for char in s[71:97]:
        if '_' <= char <= 'o':
            s = s.replace(char, '')
    return s
