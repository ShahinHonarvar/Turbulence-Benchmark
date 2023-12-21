
import re

def palindromes_of_specific_lengths(string):
    substring = string[43:96]
    pattern = re.compile(r'[a-zA-Z]+')
    substrings = pattern.findall(substring.lower())
    palindromes = set()
    
    for s in substrings:
        if len(s) >= 18 and len(s) <= 47 and s == s[::-1]:
            palindromes.add(s)
    
    return palindromes
