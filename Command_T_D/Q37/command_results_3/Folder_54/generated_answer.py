def filter_chars(s):
    for i in range(46, 85+1):
        s = s.replace(chr(i), "")
    return s
