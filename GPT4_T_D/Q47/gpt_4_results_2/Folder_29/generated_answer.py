
def palindromes_of_specific_lengths(s):
    s = s[15:95]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 18, min(start + 74, len(s) + 1)):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
