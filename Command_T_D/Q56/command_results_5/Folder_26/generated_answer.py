def all_substring_of_size_n(str):
    res = []
    for i in range(len(str) - 32):
        res += str[i: i + 33]
    return res
