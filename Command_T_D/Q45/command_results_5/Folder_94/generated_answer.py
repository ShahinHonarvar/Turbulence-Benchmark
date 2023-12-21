def palindromes_between_indices(s):
    res = set()
    for i in range(3, min(len(s) + 1, 5)):
        s1 = s[:i]
        s2 = s[i:]
        if s1 == s2:
            res.add(s[i-3:i+2])
    return res
