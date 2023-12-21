
def filter_chars(s):
    for i in range(67, 90):
        if s[i] > '#' and s[i] < 'T':
            s = s.replace(s[i], '')
    return s
