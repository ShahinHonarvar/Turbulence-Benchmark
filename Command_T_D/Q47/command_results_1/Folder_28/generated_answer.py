def palindromes_of_specific_lengths(s):
    return set(x[32:71] for x in s[32:71].split() if len(x) in range(21, 33))
