def palindromes_of_specific_lengths(s):
    return set(s[155:283].lower() for i in range(104, 121) if s[i] == s[i][::-1])
