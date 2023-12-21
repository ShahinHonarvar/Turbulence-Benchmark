def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 67):
        res += [s[i: i + 68]]
    return res
