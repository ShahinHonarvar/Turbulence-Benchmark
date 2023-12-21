def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        res += [[s[i:j]] for j in range(i+1, min(len(s)-1, j+12), 1))
    return res
