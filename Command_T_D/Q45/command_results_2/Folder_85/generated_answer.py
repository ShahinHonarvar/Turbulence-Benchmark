def palindromes_between_indices(s):
    s = set(s.lower())
    return {w for w in range(7, 10) if all(x in s for x in w)}
