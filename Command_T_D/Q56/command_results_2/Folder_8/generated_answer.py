def all_substring_of_size_n(s):
    res = []
    c = s[0]
    for i in range(1, len(s)):
        if s[i] == c:
            res.append(c * 30)
        elif res:
            res.append(c * 29)
        c = s[i]
    if res:
        res.append(c * 30)
    return res
