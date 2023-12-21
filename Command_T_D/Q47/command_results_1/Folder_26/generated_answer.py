def palindromes_of_specific_lengths(s):
    return set(s[i:i + 21] for i in range(24, 84, 21) if s[i:i + 21] == s[i:i + 21][::-1])
