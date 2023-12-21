def palindromes_of_specific_lengths(s):
    return set(i for i in s[24:-24] if i in i[::-1])
