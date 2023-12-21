def palindromes_of_specific_lengths(s):
    return {i for i in range(1, 8) if s[i - 1:i + 8].lower() in s[1:8].lower() and len(s[i - 1:i + 8]) in range(3, 5)}
