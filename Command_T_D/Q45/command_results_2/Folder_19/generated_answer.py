def palindromes_between_indices(s):
    indices = range(1, 8)
    return set(map(str.lower, (s[i:j] for i in indices for j in indices)))
