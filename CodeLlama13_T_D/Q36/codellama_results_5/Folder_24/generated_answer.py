
def filter_chars(s):
    for i in range(10, 15):
        if s[i] > 't' and s[i] < 'v':
            s = s.replace(s[i], '')
    return s
