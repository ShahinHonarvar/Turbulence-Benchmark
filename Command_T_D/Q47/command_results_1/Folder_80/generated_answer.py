def palindromes_of_specific_lengths(s):
    return {s[i:i+25] for i in range(35, 88, 25) if s[i:i+25].lower() == s[i:i+25][::-1].lower()}
