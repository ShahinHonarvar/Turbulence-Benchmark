def remove_repeat_chars(s):
    res = ""
    for c in s:
        if c not in res:
            res += c
    return res
