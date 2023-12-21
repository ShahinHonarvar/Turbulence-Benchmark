def filter_chars(s):
    for i in range(63, 85):
        if s[i] >= 'E' and s[i] <= '~':
            s = s.replace(s[i], '')
    return s
