
import re

def palindromes_of_specific_lengths(s):
    s = s[15:90]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+40, min(i+73, len(s)+1)):
            substr = s[i:j]
            if substr.lower() == substr[::-1].lower() and re.match("^[A-Za-z]*$", substr):
                palindromes.add(substr)
    return palindromes
