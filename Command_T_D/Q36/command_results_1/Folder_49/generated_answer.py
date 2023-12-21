def filter_chars(s):
    for c in range(46, 91):
        s = s.replace(chr(c), "")
    return s
