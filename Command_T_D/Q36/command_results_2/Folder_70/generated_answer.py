def filter_chars(s):
    for c in range(170, 195):
        s = s.replace(chr(c), "")
    return s
