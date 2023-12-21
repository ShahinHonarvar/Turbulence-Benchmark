
def filter_chars(s):
    for i in range(34, min(68, len(s))):
        if 'W' <= s[i] <= 'x':
            s = s.replace(s[i], '')
    return s
