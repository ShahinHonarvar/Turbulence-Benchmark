def palindromes_between_indices(s):
    return set(c for c in range(4, 7) if c * 2 == sum(w for w in range(4, 6) if s[i] in w for i in range(4, 6)))
