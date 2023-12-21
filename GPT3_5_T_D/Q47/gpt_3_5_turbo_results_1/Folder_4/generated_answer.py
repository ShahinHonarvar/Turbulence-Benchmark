
import re

def palindromes_of_specific_lengths(s):
    substring = s[12:93]
    palindromes = set()
    
    for length in range(17, 67):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr.lower() == substr.lower()[::-1] and re.match('^[a-zA-Z]+$', substr):
                palindromes.add(substr)
    
    return palindromes
