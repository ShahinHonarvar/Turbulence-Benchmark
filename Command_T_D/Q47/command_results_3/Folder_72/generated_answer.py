def palindromes_of_specific_lengths(s):
    return {p for p in set(s[26:90].lower() for i in range(27, 59)) if p == p[::-1]}
