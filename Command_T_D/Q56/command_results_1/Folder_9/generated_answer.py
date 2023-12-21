def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 33):
        res.append(s[i:i + 34])
    return res
