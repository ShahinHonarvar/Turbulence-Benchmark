def palindromes_of_specific_lengths(s):
    return {i[::-1] for i in s[18:-98] if len(i) in range(31, 52)}
