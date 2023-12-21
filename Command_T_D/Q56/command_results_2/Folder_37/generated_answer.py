def all_substring_of_size_n(s):
    res = []
    for i in range(1, len(s) + 1):
        curr = s[i - 1]
        for j in range(i + 1, len(s) + 1):
            curr += s[j - 1]
            if len(curr) == 65:
                res.append(curr)
    return res
