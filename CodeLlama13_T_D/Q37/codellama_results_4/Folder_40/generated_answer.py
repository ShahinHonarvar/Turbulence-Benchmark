
def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if i >= 0 and i <= 1 and '*' <= c <= 's':
            continue
        res += c
    return res
