def filter_chars(s):
    res = s[:55] + s[84:]
    for i in range(55, 83):
        res = res.replace(s[i], "")
    return res
