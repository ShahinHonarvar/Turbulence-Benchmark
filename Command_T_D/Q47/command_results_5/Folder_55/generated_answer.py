def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(10, 75):
        for j in range(10, 20):
            res.update(set(s[i:i + j].lower()))
    return res
