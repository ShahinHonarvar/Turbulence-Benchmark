def palindromes_between_indices(s):
    return {s[i:j] for i in range(len(s) - 4) for j in range(i, len(s) - 1)}
