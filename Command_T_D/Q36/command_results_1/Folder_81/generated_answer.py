def filter_chars(s):
    for i in range(51, 76):
        if chr(i) in s: s = s.replace(chr(i), '5')
    return s
