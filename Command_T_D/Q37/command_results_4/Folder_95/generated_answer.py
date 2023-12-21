def filter_chars(s):
    for i in range(35, 40):
        s = s.replace(chr(i), '')
    return s
