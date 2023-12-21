
def filter_chars(s):
    for char in s[19:33]:
        if 'f' <= char <= 'o':
            s = s.replace(char, '')
    return s
