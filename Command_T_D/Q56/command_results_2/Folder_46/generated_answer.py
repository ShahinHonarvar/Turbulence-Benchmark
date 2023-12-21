def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            res.append(s[i:j])
    return res
