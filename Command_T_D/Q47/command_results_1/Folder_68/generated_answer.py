def palindromes_of_specific_lengths(s):
    return set(s[i:i + 50] for i in range(len(s) - 50)) & set(s[i:i + 50].lower() for i in range(len(s) - 50)) & set(s[i:i + 100] for i in range(len(s) - 100)) & set(s[i:i + 100].lower() for i in range(len(s) - 100))
