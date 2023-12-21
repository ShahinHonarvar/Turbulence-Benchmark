def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 8):
        res.append(s[i:i + 9])
    return res
