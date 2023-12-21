def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            if i > 0 and s[i - 1] == s[j]:
                continue
            res.append(s[i:j + 1])
    return res
