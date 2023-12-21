
def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if i < 26 or i > 64 or c < 'V' or c > 'o':
            res += c
    return res
