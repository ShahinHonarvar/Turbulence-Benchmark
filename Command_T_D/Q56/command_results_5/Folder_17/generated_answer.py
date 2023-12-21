def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            res += [s[i:j+1]]
    return res
