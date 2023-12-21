def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 44):
        tmp = s[i:i + 45]
        if tmp not in res:
            res.append(tmp)
    return res
