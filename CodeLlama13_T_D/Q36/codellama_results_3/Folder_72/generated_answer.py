
def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if 'W' <= c < 'x':
            res += c
    return res
