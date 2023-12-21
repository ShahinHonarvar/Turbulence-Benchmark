def remove_repeat_chars(s):
    res = s[:39] + s[43:]
    for i in range(len(res)):
        if res[i] in res[:i]:
            res = res.replace(res[i], '')
    return res
