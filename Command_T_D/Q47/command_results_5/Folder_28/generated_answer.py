def palindromes_of_specific_lengths(s):
    return set(x for x in s[32:-1] if len(x) in (21,22,23,24,25,26,27,28,29,30,31,32))
