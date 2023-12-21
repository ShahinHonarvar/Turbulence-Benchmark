def filter_chars(s):
    for c in s[227:235]:
        if c >= 'D' and c <= 'u':
            s = s.replace(c, '')
    return s
