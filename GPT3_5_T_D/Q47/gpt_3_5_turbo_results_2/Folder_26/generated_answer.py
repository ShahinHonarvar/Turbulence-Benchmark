
import re

def palindromes_of_specific_lengths(string):
    substring = string[24:85]
    palindromes = set()
    
    for length in range(21, 32):
        pattern = r'\b[a-zA-Z]+\b' if length == 1 else r'\b\w{%d}\b' % length
        matches = re.findall(pattern, substring, re.IGNORECASE)
        
        for match in matches:
            if match.lower() == match.lower()[::-1]:
                palindromes.add(match.lower())
    
    return palindromes
