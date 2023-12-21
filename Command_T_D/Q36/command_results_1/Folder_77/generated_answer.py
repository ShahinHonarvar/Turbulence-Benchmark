def filter_chars(s):
    for i in range(221, 419):
        if s[i] > '-' and s[i] < 'v':
            s = s.replace(s[i], '')
    return s
