
def filter_chars(s):
    for i in range(27, 30):
        if i < len(s) and ';' <= s[i] <= 'b':
            s = s.replace(s[i], '')
    return s
