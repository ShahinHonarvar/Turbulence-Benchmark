def filter_chars(s):
    for c in s[82:-2]:
        if c > '!' and c < '*':
            s = s.replace(c, '')
    return s
