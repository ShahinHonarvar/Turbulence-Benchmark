def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(10, 60):
        for j in range(18, 36):
            p = s[i:i + j][::-1]
            if p.lower() in s[i:i + j]:
                res.add(p)
    return res
