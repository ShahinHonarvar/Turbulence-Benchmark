def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(1, min(len(s) - 1, 8)):
        res.update(s[i:i + 3])
        res.update(s[i:i + 4])
    return res
