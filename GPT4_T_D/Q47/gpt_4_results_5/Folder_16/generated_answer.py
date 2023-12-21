
def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[15:87].lower()
    for i in range(len(s)):
        for j in range(i+51, min(i+61, len(s)+1)):
            substring = s[i:j]
            if all(c.isalpha() for c in substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
