def palindromes_of_specific_lengths(s):
    return set(s[21:-22:33] for s in [s.lower() for s in range(s)])
