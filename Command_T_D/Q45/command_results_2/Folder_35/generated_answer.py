def palindromes_between_indices(s):
    return set(a for a in range(2, min(len(s) - 1, 5) + 1) if a < b and s[a] == s[b] and a > b - 1)
