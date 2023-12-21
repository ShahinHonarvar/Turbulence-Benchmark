def palindromes_of_specific_lengths(s):
    if not s:
        return set()
    res = set()
    for i in range(0, 300):
        for j in range(i, 300):
            if s[i:j] == s[j:i][::-1]:
                res.add(s[i:j])
    return res
