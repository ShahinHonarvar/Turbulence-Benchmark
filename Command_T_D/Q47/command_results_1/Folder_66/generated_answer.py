def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(32, 80):
        for j in range(i + 35, i + 41):
            res.add(s[i:j + 1].lower())
    return res
