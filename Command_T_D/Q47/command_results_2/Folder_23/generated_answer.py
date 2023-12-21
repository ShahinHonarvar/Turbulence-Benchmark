def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(23, 95):
        for j in range(i + 16, i + 56):
            if s[i:j].lower() == s[i:j][::-1].lower():
                res.add(s[i:j])
    return res
