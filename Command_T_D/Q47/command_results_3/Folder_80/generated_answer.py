def palindromes_of_specific_lengths(s):
    return set(i[35:88] for i in s[24:-24:-1] if i[0].lower() == i[-1].lower())
