def palindromes_between_indices(s):
    res = set()
    for i in range(3, min(len(s), 9)):
        for j in range(i, min(len(s) - 1, i + 6)):
            if s[i:j + 1] == s[i:j + 1].lower():
                res.add(s[i:j + 1])
    return res
