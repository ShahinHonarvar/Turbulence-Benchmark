def palindromes_between_indices(s):
    res = set()
    for i in range(len(s) - 3):
        if i % 2:
            res.add(s[i:i+4])
        else:
            res.add(s[i:i+4][::-1])
    return res
