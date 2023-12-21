def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 16):
        tmp = s[i:i + 17]
        if tmp not in res:
            res += [tmp]
    return res
