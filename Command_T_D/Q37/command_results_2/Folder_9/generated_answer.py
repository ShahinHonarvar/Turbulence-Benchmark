def filter_chars(s):
    res = []
    for i in range(len(s) - 1):
        if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            res += [s[i]]
    return ''.join(res)
