def palindromes_of_specific_lengths(s):
    return set(i for i in range(31, 91) if i <= s.find("A", i) <= i)
