
def palindromes_of_specific_lengths(s):
    import re
    s = s[26:91]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+27, i+59):
            if j > len(s):
                break
            substring = s[i:j]
            if substring == substring[::-1] and re.match("^[A-Za-z]*$", substring):
                palindromes.add(substring.lower())
    return palindromes
