
def filter_chars(s):
    for i in range(35, 98+1):
        c = s[i]
        if 'A' <= c <= 'z':
            s = s.replace(c, '')
    return s
