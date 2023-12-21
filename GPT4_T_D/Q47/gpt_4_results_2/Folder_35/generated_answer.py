
import re

def palindromes_of_specific_lengths(s):
    s = s[34:91]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 14, min(i + 40, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.search("^[A-Za-z]*$", substring):
                palindromes.add(substring.lower())
    return palindromes
