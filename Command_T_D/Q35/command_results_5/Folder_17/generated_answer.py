def remove_repeat_chars(s):
    res = s[0:73] + s[84:]
    for i in range(73, 84):
        res = res.replace(s[i], "")
    return res
