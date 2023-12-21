
def filter_chars(s):
    for i in range(24, 83):
        if i < len(s) and 'f' < s[i] < 'o':
            s = s.replace(s[i], '')
    return s
