def remove_repeat_chars(s):
    res = ""
    for c in s[330:543]:
        if c not in res:
            res += c
    return res
