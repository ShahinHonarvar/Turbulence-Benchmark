def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 77):
        res.append(s[i:i + 78])
    return res
