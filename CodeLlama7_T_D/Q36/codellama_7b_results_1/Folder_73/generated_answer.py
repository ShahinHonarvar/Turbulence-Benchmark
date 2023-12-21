
def filter_chars(s):
    for i in range(66, 91):
        s = s.replace(chr(i), "")
    return s
