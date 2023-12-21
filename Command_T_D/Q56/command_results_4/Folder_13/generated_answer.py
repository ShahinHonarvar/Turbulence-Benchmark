def all_substring_of_size_n(s):
    res = []
    for i in range(1, len(s) + 1):
        temp = []
        for j in range(i):
            if s[j] not in temp:
                temp.append(s[j])
        if len(temp) == i:
            res += [temp]
    return res
