def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        if len(s[:i+52]) == 52:
            res.append(s[:i+52])
    return res
