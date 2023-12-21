def palindromes_of_specific_lengths(s):
    return {i for i in range(len(s)-20, len(s)-74, 2) if s[i:i+40] in set(s[i:i+40].lower())}
