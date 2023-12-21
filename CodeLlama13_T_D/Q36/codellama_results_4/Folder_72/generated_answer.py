
def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if 44 < ord(c) < 68:
            res += c
    return res
