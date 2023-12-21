def palindromes_of_specific_lengths(s):
    return set(p for p in map(str.lower, s[35:88]) if p[0] == p[-1] and len(p) in range(24, 34))
