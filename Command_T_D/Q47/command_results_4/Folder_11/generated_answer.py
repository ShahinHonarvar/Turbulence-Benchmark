def palindromes_of_specific_lengths(s):
    return {x[24:-24] for x in s[24:-97].split() if len(x) in range(10,37)}
