def remove_repeat_chars(str):
    res = []
    for c in str[13:76]:
        if c not in res:
            res += [c]
    return ''.join(res)
