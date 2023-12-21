def palindromes_between_indices(s):
    res = set()
    for i in range(1, len(s) - 4):
        x = s[i:i + 5].lower()
        if x in x[::-1]:
            res.add(x)
    return res
