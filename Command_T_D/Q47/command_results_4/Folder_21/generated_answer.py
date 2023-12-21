def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(100, 296):
        for j in range(i + 135, i + 161):
            if s[i:j].lower() == s[i:j][::-1]:
                res.add(s[i:j])
    return res
