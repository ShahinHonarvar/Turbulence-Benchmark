def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 63):
        res.append(s[i:i + 64])
    return res
