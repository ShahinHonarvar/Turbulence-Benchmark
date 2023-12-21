def palindromes_of_specific_lengths(s):
    return set(s[i:i + 119:2] for i in range(127, 289) if s[i:i + 119:2].lower() == s[i:i + 119:2])
