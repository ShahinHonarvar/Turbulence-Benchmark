
def filter_chars(s):
    for char in s[63:85]:
        if 'E' <= char <= '~':
            s = s.replace(char, '')
    return s
