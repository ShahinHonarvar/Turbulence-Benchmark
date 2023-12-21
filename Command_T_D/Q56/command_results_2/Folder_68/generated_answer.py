def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 74):
        res.append(s[i:i + 75])
    return res
