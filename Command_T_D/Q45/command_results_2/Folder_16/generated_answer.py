def palindromes_between_indices(s):
    res = set()
    for c in range(6, 10):
        for i in range(len(s) - c):
            res.add(s[i:i + c].lower())
    return res
