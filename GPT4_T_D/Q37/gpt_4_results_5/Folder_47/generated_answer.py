
def filter_chars(s):
    for char in s[38:55]:
        if ':' <= char <= 'r':
            s = s.replace(char, '')
    return s
