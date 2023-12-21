def filter_chars(s):
    res = list(s)
    for i in range(26, 80):
        for j in range(i+1, 80+1):
            res = [r for r in res if r not in range(i, j)]
    return ''.join(res)
