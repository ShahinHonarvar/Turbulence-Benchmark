def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(15, 73):
        for j in range(i + 19, i + 56):
            if s[i] == s[j]:
                res.add(s[i:j])
    return res
