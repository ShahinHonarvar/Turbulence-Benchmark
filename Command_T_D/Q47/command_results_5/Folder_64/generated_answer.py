def palindromes_of_specific_lengths(s):
    return {p for p in s[0:7] if p in s[::-1] and len(p) in (4, 5)}
