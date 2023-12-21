def palindromes_between_indices(s):
    res = set()
    for i in range(1, 5):
        res.update(set(s[0:i] + s[i:]))
    return res
