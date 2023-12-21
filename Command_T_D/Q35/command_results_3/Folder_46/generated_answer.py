def remove_repeat_chars(s):
    i = 10
    j = 79
    c = ''
    res = ''
    for c in s:
        if c in c:
            continue
        elif c not in res:
            res += c
    return res
