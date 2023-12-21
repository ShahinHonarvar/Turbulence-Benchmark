def filter_chars(s):
    for i in range(1, 8):
        if s[i] > '3' and s[i] < '^':
            s = s.replace(s[i], '')
    return s
