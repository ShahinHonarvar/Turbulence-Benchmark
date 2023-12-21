def palindromes_between_indices(s):
    return set(i[::-1] for i in range(3, min(len(s), 7) + 1)) & set(s[0:6].lower())
