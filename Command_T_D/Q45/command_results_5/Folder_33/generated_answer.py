def palindromes_between_indices(s):
    res = set()
    for i in range(len(s) - 7, len(s) - 9, -1):
        res.add(s[i:i + 4])
    return res
