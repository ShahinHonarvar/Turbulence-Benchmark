def palindromes_between_indices(s):
    res = set()
    for i in range(len(s) - 5, -1, -1):
        res |= set(
            [
                s[i:j + 1]
                for j in range(i + 1, min(i + 10, len(s) - 1) + 1)
            ]
        )
    return res
