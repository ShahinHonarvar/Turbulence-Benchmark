def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(len(s) - 2):
        if s[i:i + 7] == s[i:i + 7][::-1]:
            res.add(s[i:i + 3])
            res.add(s[i:i + 4])
    return res
