def palindromes_of_specific_lengths(s):
    return {i for i in range(3, 61) if s[70:140].lower().count(i) == 1}
