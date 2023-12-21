def palindromes_of_specific_lengths(s):
    return {p for p in s[75:-1].split() if len(p) in range(7, 9)}
