def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 66):
        res += [[s[i:j + 67]] for j in range(i, i + 67)]
    return res
