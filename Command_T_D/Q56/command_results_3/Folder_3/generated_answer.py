def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 92):
        res.append(s[i:i + 93])
    return res
