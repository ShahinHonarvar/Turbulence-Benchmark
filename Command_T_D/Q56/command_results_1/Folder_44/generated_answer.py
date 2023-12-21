def all_substring_of_size_n(str):
    res = []
    for i in range(len(str)):
        res += [str[i:]]
    return list(set(res))
