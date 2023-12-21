def palindromes_of_specific_lengths(s):
    return set(x[15:-15] for x in s[15:-89].lower() if len(x) in range(40,73))
