def remove_repeat_chars(s):
    res = ''
    for i in range(len(s) - 6):
        res += s[i]
    for j in range(len(s) - 6, len(s)):
        if s[j] in res:
            res = res.replace(s[j], '')
        else:
            res += s[j]
    return res
