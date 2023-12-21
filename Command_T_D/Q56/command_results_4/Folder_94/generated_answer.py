def all_substring_of_size_n(s):
    if len(s) < 70:
        return []
    res = []
    for i in range(len(s) - 69):
        res += [s[i:i + 70]]
    return res
