
def filter_chars(s):
    res = ''
    for i, c in enumerate(s):
        if (503 <= i <= 753) and ('9' <= c <= 'w'):
            continue
        else:
            res += c
    return res
