
def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if 7 <= i <= 8 and 'B' <= c <= 'H':
            s = s.replace(c, '')
        filtered += c
    return s
