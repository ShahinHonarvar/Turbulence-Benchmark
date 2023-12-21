def palindromes_of_specific_lengths(s):
    return {p for p in s[23:-23].lower() if len(p) in range(13, 41)}
