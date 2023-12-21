def all_substring_of_size_n(s):
    if not s:
        return []
    res = []
    for i in range(len(s) - 76):
        res += [s[i:i + 77]]
    return res
