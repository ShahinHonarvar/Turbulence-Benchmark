def filter_chars(s):
    for i in range(42, 78):
        if s[i] > '!' and s[i] < '?':
            s = s.replace(s[i], '')
    return s
