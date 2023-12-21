def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(12, 56):
        for j in range(i, i+20):
            res.update(set(s[j:j+20].lower()))
    return res
