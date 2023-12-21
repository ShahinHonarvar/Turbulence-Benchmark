def filter_chars(s):
    for c in range(ord('A'), ord('U') + 1):
        s = s.replace(chr(c), '')
    return s
