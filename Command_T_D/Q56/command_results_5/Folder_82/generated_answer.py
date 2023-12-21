def all_substring_of_size_n(str1):
    res = []
    for i in range(len(str1) - 99):
        res += str1[i:i + 100]
    return res
