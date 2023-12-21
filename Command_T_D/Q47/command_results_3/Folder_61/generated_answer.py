def palindromes_of_specific_lengths(s):
    return set(x for x in s.lower() if x in s[0:30][::-1])
