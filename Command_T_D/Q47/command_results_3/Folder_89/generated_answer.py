def palindromes_of_specific_lengths(s):
    return set(s[i:j] for i in range(18, 88) for j in range(i, min(len(s)-1, 88)))
