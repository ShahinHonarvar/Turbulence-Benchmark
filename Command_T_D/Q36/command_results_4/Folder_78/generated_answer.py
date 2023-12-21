def filter_chars(s):
    res = ""
    for i in range(29, 33):
        res += s[i]
        if res[0] >= '%' and res[0] <= 'a':
            res = res.replace(res[0], "")
    return res
