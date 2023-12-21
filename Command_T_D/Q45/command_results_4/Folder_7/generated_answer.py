def palindromes_between_indices(s):
    return set(i for i in range(1, len(s) + 1) if s[i - 1] == s[i])
