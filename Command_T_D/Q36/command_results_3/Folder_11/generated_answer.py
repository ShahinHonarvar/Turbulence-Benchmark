def filter_chars(s):
    for i in range(86, 93):
        if s[i] > 'E' and s[i] < '~':
            s = s.replace(s[i], '')
    return s
