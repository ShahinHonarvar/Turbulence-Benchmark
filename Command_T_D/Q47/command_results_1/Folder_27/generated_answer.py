def palindromes_of_specific_lengths(s):
    return set(i for i in range(13, 99) if i < s.lower().index("a") + 26 <= i + 29 and s[i - 26:i + 29] == s[i + 29:i - 26])
