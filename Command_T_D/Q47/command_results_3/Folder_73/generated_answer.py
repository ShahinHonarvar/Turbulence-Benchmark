def palindromes_of_specific_lengths(s):
    return {p for p in s[21:-1].lower() if len(p) in range(22, 34)}
