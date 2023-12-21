def palindromes_between_indices(s):
    res = set()
    for i in range(len(s) - 5, -1, -1):
        for j in range(i, i + 5):
            if i == j:
                continue
            res.update(set(s[i:j] + s[j:i] + s[i:j][::-1] + s[j:i][::-1]))
    return res
