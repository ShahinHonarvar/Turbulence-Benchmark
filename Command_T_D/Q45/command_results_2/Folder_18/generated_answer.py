def palindromes_between_indices(s):
    return set(s[i:j] for i in range(1, 7) for j in range(i, 7))
