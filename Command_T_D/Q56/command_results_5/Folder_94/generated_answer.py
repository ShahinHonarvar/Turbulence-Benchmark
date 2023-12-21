def all_substring_of_size_n(s):
    if len(s) < 70:
        return []
    res = []
    for i in range(70):
        res += [[s[j:j + 70]] for j in range(i, len(s), 70)]
    return list(set(res))
