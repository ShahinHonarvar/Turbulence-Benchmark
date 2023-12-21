def palindromes_of_specific_lengths(s):
    return set(s[29:96].lower() for i in range(12, 19) if s[i:i+2].lower() == s[i:i+2][::-1].lower())
