def palindromes_between_indices(s):
    res = set()
    for c in s[3:-2]:
        for i in range(len(res)):
            res.add(c + res[i][::-1])
        res.add(c + c[::-1])
    return res
