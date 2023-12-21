def palindromes_of_specific_lengths(s):
    return {x[18:87] for x in s.lower() if len(x) in (38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60)}
