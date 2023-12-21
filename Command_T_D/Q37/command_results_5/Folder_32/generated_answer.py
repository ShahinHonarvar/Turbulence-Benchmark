def filter_chars(s):
    for c in s[23:89]:
        if c >= 'w' and c <= '{':
            s = s.replace(c, '')
    return s
