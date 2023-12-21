def palindromes_of_specific_lengths(s):
    return set(p for p in s[28:94].lower() if len(p) in range(38, 49))
