def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(13, 95):
        for j in range(i + 57, i + 60):
            if s[i][j] == s[i][j][::-1]:
                res.add(s[i][j])
    return res
