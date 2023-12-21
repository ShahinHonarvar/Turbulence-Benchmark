def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(12, 56):
        for j in range(20, 21):
            res.update(set(s[i:i+j].lower() for s in s[i:i+j][::-1] if s))
    return res
