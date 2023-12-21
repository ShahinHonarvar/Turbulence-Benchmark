def palindromes_of_specific_lengths(s):
    return set(x[::-1] for x in s[127:288][119:-1])
