def palindromes_between_indices(s):
    return set(s[i:i+3] for i in range(1, len(s)-3))
