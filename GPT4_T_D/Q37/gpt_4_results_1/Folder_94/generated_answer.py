
def filter_chars(s):
    for char in set(s[51:97]):
        if 'X' <= char <= 'p':
            s = s.replace(char, '')
    return s
