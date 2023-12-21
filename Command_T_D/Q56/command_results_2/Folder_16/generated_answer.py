def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 125):
        res.append(s[i:i + 124])
    return res
