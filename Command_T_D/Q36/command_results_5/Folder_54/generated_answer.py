def filter_chars(s):
    for i in range(18, 38):
        if s[i] in 'QWRTYPSDFGHJKL':
            s = s.replace(s[i], '')
    return s
