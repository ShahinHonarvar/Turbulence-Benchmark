def palindromes_of_specific_lengths(s):
    return set(s[i:i+20].lower() for i in range(0,len(s)-20) if len(s[i:i+20]) in range(5,81))
