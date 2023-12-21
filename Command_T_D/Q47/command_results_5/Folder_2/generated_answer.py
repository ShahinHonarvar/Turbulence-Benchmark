def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(10, 60):
        for j in range(i, i+18, -1):
            if s[j:j+18] == s[j:j+18][::-1]:
                res.add(s[j:j+18])
    return res
