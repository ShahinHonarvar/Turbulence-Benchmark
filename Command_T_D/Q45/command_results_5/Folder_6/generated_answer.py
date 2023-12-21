def palindromes_between_indices(s):
    res = set()
    for i in range(4, 8):
        for j in range(i):
            res.add(s[j:i])
    return res
