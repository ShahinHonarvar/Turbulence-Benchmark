def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(31, 75):
        for j in range(i, i + 23, -1):
            if s[j:j + 23] == s[j:j + 23][::-1]:
                res.add(s[j:j + 23])
    return res
