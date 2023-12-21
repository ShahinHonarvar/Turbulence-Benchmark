def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 15):
        res += [s[i:i + 16]]
    return res
