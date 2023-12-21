
def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if i >= 40 and i < 63 and ord(c) > 7 and ord(c) < 72:
            continue
        else:
            res += c
    return res
