def remove_repeat_chars(s):
    res = []
    for i in range(90, 200):
        res += [c for c in s[i] if c not in res]
    return ''.join(res)
