def palindromes_of_specific_lengths(s):
    return set(i[16:94] for i in s[16:94] if i[0] in 'a-z' and i[1:].lower() == i[::-1])
