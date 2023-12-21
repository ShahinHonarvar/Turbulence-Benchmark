def all_substring_of_size_n(s):
    if len(s) < 23:
        return []
    res = []
    for i in range(len(s) - 22):
        res.append(s[i:i + 23])
    return res
