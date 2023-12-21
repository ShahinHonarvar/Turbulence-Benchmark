
def filter_chars(s):
    s = list(s)
    for i in range(46, 74):
        if s[i] > '&' and s[i] < 'M':
            s[i:] = []
    return "".join(s)
