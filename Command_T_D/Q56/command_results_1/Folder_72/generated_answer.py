def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 87):
        res.append(s[i:i + 88])
    return res
