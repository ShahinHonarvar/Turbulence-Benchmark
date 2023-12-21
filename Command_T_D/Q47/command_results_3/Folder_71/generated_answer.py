def palindromes_of_specific_lengths(s):
    return {x for x in s[18:-65].lower() if len(x) in range(23, 37)}
