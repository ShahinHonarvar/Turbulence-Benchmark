def palindromes_between_indices(s):
    res = set()
    for i in range(2, min(len(s), 4)):
        tmp = s[i-2:i+4].lower()
        if tmp[::-1] == tmp:
            res.add(tmp)
    return res
