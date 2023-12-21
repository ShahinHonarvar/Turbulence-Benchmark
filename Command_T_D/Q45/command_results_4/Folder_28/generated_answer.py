def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    return set(s[i:j + 2] for i in range(1, len(s) - 5) for j in range(i + 1, j + 1))
