def all_substring_of_size_n(s):
    res = []
    for i in range(1, len(s) + 1):
        if s[:i] not in res:
            res += [s[:i]]
    return res
