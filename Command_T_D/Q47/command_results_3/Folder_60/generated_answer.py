def palindromes_of_specific_lengths(s):
    return set(i for i in s[23:-23][32:-34] if i == i[::-1])
