
def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[43:96]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 17, min(i + 48, len(s) + 1)):
            substring = s[i:j]
            if not any(not c.isalpha() for c in substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
