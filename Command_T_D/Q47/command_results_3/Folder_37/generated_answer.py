def palindromes_of_specific_lengths(s):
    return set(filter(lambda x: 3 <= len(x) <= 5, map(str.lower, s[0:10])))
