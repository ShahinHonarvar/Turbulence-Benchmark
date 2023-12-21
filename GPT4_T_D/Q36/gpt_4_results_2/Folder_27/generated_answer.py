
def filter_chars(s):
    for i in range(49, 75):
        if s[i] > '6' and s[i] < '_':
            s = s.replace(s[i], '')
    return s
