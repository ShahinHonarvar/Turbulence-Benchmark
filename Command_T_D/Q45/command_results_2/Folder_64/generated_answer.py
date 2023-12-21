def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    indices = list(range(len(s) - 4, len(s) - 1))
    return set(x for x in range(5, len(s) - 4) if indices[x - 5] <= x < indices[x + 5] and s[x - 5] in s[x + 5])
