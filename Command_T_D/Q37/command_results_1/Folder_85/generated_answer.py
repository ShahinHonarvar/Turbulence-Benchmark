def filter_chars(s):
    for c in range(ord('O'), ord('d') + 1):
        s = s.replace(chr(c), '')
    return s
