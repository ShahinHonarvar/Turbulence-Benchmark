def palindromes_between_indices(s):
    return set(s[i:j] for i in range(4, 9) for j in range(i, 9))
