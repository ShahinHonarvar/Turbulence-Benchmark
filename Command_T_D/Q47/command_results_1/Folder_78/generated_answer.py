def palindromes_of_specific_lengths(s):
    return {p for p in s[15:72].lower() if len(p) in range(19, 55)}
