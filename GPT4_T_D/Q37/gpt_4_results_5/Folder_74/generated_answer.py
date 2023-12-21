
def filter_chars(s):
    for i in range(19, 33):
        if 'f' <= s[i] <= 'o':
            s = s.replace(s[i], '')
    return s
