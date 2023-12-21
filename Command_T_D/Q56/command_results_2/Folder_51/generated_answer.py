def all_substring_of_size_n(s):
    res = []
    for c in s:
        res += [[c]]
        res += [[i for i in range(len(res[0]))]]
    return res
