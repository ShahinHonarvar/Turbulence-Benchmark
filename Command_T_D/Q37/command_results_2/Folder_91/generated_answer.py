def filter_chars(s):
    res = s[:7] + s[8:]
    for c in range('B', 'H'):
        res = res.replace(c, '')
    return res
