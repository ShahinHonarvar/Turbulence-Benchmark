def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(10, 70):
        for j in range(24, 52):
            res.update(set(s[i:i + j].lower() if i + j <= len(s) - 1 else []))
    return res
