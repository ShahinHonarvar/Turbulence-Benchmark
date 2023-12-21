
import re

def palindromes_of_specific_lengths(s):
    s = s[3:301]
    s = re.sub("[^a-z]", "", s.lower())
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 30, min(start + 301, len(s))):
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
