def palindromes_between_indices(s):
    letters = set(s.lower()[:9])
    return set(a for a in range(len(s) - 7, -1, -1) if a[::-1] in letters)
