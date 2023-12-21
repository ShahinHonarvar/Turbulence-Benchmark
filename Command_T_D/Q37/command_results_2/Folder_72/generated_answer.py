def filter_chars(s):
    for i in range(35, 51):
        s = s.replace('H', 's', i)
    return s
