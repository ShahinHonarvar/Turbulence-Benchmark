def palindromes_between_indices(s):
    res = set()
    for i in range(len(s) - 4):
        for j in range(i + 4, len(s)):
            res.update(set(s[i:j + 1].lower()))
    return res
