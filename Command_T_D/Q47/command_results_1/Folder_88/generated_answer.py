def palindromes_of_specific_lengths(s):
    return {p for p in s[11:-11].lower() if len(p) in range(4, 6)}
