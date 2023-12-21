def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(12, 220):
        j = i // 2
        while j < 122:
            if s[i][j] == s[i][-j-1]:
                res.add(s[i][:j] + s[i][-j:-1] + s[i][j+1:-1])
    return res
