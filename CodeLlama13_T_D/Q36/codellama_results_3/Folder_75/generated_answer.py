
def filter_chars(s):
    new_str = ''
    for i in range(46, 75):
        if s[i] > '&' and s[i] < 'M':
            new_str += s[i]
    return new_str
