def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            for k in range(j, len(s)):
                res.append(s[i:j+1])
    return res
