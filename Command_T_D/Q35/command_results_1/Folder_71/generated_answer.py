def remove_repeat_chars(s):
    res = ''
    for c in s[20:35]:
        if c not in res:
            res += c
    return res
