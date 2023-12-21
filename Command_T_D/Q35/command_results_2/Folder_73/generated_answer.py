def remove_repeat_chars(s):
    res = ""
    for c in s:
        if c not in res and c in s[10:76]:
            res += c
    return res
