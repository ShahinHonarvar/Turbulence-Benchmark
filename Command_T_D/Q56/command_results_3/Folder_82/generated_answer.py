def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 99):
        res += [[s[j:j + 100] for j in range(i, i + 100)]]
    return res
