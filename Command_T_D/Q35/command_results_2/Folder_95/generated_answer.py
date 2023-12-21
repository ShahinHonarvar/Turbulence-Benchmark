def remove_repeat_chars(s):
    res = ""
    for i in s:
        if i in res:
            continue
        else:
            res += i
    return res
