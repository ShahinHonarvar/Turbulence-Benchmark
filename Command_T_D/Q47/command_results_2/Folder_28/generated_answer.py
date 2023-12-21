def palindromes_of_specific_lengths(s):
    return set(i[32:71] for i in s[32:-1] if i[::-1] == i)
