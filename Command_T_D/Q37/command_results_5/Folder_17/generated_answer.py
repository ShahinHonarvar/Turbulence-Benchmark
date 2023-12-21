def filter_chars(s):
    for i in range(27, 29):
        if s[i] >= ';' and s[i] <= 'b':
            s = s.replace(s[i], '')
    return s
