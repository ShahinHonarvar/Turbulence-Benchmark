def palindromes_of_specific_lengths(s):
    res = set()
    for l in range(12, 18):
        for i in range(29, 96):
            if i + l >= len(s):
                break
            if s[i:i + l] == s[i + l:]:
                res.add(s[i:i + l])
    return res
