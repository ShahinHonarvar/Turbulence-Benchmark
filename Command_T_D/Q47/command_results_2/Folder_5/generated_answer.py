def palindromes_of_specific_lengths(s):
    return set(s[63:70].lower() for i in range(4, 6) if i*2 == len(s[63:70]))
