def filter_chars(s):
    for c in range(ord('a'), ord('i') + 1):
        s = s.replace(chr(c), '')
    return s
