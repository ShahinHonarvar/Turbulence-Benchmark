def palindromes_between_indices(s):
    res = set()
    for c in s[0:4]:
        for i in range(2, 7):
            res.update(set(str(i * c + s[0:4])))
    return res
