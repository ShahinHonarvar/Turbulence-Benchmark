
import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = r'[a-z]+'
    matches = re.findall(pattern, string.lower())
    
    for match in matches:
        if len(match) == 445 and match == match[::-1]:
            palindromes.add(match)
    
    return palindromes
