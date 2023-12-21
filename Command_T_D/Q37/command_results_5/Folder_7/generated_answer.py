def filter_chars(s):
    for i in range(521, 722):
        if s[i] >= '>' and s[i] <= '_':
            s = s.replace(s[i], '')
    return s
