
import re

def palindromes_of_specific_lengths(s):
    s = s[15:87]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 51, min(i + 61, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and re.match('^[a-zA-Z]*$', substring):
                palindromes.add(substring.lower())
    return palindromes
