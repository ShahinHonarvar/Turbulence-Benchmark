def filter_chars(s):
    i = 18
    while i < len(s):
        if s[i] > 'K' and s[i] < 'a':
            s = s.replace(s[i], '')
        i += 1
    return s
