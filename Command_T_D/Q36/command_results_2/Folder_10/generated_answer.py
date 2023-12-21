def filter_chars(s):
    for i in range(35, 61):
        if s[i] > '!' and s[i] < 'B':
            s = s.replace(s[i], '')
    return s
