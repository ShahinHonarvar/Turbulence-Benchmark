def palindromes_between_indices(s):
    res = set()
    for lst in range(5, len(s) - 1):
        for idx in range(4, lst - 1):
            if idx == lst - 1:
                res.add(s[idx:lst + 1])
            else:
                res.add(s[idx:lst + 1] + s[lst:idx + 1])
    return res
