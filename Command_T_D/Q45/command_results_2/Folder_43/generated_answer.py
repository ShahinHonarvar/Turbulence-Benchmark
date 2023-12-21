def palindromes_between_indices(s):
    res = set()
    for i in range(2, 6):
        res.update(s[i - 2:i + 5].lower() for s in range(s[i - 2], s[i + 5]))
    return res
