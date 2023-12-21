def remove_repeat_chars(s):
    res = s[0:6] + s[9:]
    for i in range(6, 9):
        res = res.replace(s[i], "")
    return res
