def palindromes_of_specific_lengths(s):
    return set(p for p in s[39:94].lower() if len(p) in range(14, 53))
