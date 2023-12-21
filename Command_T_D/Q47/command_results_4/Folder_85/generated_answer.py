def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(29, 98):
        if s[i: i + 6] == s[i: i + 6][::-1]:
            res.add(s[i: i + 6])
    return res
