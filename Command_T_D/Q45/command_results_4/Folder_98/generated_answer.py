def palindromes_between_indices(s):
    return set(s[3:5] + s[::-1][3:-1])
