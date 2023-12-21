def palindromes_between_indices(s):
    s = s.lower()
    return set(
        ''.join(sorted(x))
        for x in range(len(s) - 4, -1, -1)
        if len(set(x)) >= 6
    )
