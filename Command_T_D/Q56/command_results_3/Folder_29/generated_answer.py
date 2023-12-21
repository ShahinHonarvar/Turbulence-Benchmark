def all_substring_of_size_n(str1):
    res = []
    for i in range(len(str1) - 94):
        res.append(str1[i:i + 95])
    return res
