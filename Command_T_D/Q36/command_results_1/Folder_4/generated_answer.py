def filter_chars(s):
    for c in s[42:-2]:
        if c > '6' and c < 'g':
            s = s.replace(c, '')
    return s
