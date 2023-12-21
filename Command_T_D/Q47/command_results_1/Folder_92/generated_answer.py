def palindromes_of_specific_lengths(s):
    return set(s[0:4].lower() for i in range(3, 5) if s[i-1:i+2].lower() == s[i+1:i+4].lower())
