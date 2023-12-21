def palindromes_between_indices(s):
    return {p for i in range(4, len(s) - 1) for p in set(s[i:j] for j in range(i + 1, j + 1) if p[::-1] == p)}
