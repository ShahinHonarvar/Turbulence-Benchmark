def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        res += [s[i:i + 32]]
    return res
