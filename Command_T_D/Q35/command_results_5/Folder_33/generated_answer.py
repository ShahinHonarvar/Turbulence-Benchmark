def remove_repeat_chars(s):
    res = ""
    for i in range(125, 825):
        if s[i] in res:
            continue
        else:
            res += s[i]
    return res
