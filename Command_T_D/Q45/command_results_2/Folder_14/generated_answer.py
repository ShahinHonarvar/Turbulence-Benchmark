def palindromes_between_indices(s):
    if not s:
        return set()
    return set(p for p in (s[i:j] for i in range(len(s) - 3, -1, -1) for j in range(i + 1, j + 1)))
