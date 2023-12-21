def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 59):
        res.append(s[i:i + 60])
    return res
