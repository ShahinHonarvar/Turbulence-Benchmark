
def filter_chars(s):
    for i in range(69, 87):
        if s[i] > '#' and s[i] < 'L':
            s = s.replace(s[i], '')
    return s
