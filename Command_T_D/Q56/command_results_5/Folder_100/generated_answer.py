def all_substring_of_size_n(s):
    if len(s) < 92:
        return []
    res = []
    for i in range(len(s) - 91):
        j = 0
        while j < 92:
            res.append(s[i:i + 92])
            j += 1
    return res
