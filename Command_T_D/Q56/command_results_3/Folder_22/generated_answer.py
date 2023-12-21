def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 21):
        j = i + 22
        res.append(s[i:j])
    return res
