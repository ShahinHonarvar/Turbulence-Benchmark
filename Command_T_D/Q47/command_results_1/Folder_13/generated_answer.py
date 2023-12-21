def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(13, 95):
        for j in range(i, min(len(s) - 1, i + 57)):
            c = s[j]
            if c.isalpha() and c.lower() == s[i].lower():
                res.add(s[i:j])
    return res
