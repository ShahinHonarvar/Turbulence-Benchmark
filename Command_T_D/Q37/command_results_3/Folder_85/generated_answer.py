def filter_chars(s):
    for i in range(28, 65):
        if s[i] >= 'O' and s[i] <= 'd':
            s = s.replace(s[i], '')
    return s
