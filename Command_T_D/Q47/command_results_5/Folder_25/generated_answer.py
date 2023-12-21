def palindromes_of_specific_lengths(s):
    return set(s[26:84].lower() for i in range(30, 47) if i * 2 == sum(1 for c in s[26:84].lower() if c.isalpha()))
