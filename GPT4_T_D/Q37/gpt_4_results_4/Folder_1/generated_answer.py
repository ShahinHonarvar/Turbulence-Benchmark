
def filter_chars(s):
    indices = s[41:80]
    for char in indices:
        if 'f' <= char <= '|':
            s = s.replace(char, '')
    return s
