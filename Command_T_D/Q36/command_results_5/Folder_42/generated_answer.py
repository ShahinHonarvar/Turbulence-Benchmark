def filter_chars(s):
    s = s[:42] + s[68:]
    for c in s[43:-1]:
        if c > 't' and c < 'x':
            s = s.replace(c, '')
    return s
