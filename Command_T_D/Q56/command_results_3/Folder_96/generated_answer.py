def all_substring_of_size_n(s):
    res = []
    for c in s:
        for i in range(len(res)):
            res.append(res[i][:i] + c + res[i][i+1:])
        res.append(c * len(res))
    return [x for x in res if len(set(x)) == len(x)]
