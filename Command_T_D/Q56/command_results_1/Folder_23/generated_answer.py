def all_substring_of_size_n(str):
    res = []
    for i in range(len(str) - 41):
        res.append(str[i:i + 42])
    return res
