def filter_chars(s):
    for i in range(15, 85):
        if s[i] > 'I' and s[i] < 'M':
            s = s.replace(s[i], '')
    return s
