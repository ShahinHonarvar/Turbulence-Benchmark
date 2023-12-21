def filter_chars(s):
    s = list(s)
    s[51:77] = [x for x in s[51:77] if x in 'VZ']
    s = ''.join(s)
    return s
