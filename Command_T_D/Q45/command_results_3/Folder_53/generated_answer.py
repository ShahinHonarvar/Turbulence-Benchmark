def palindromes_between_indices(s):
    res = set()
    for i in range(4, min(len(s) - 1, 8)):
        for j in range(i + 1, min(len(s) - 1, 8)):
            c = s[i:j + 1]
            if i == j:
                res.add(c)
            elif i < j:
                res.add(c + c[::-1])
    return res
