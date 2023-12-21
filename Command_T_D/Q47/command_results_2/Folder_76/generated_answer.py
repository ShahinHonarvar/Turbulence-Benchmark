def palindromes_of_specific_lengths(s):
    return {i for i in range(101, 292) if i + 154 <= len(s) and s[i] == s[i + 154]]
