
import re

def palindromes_of_specific_lengths(string):
    substring = string[23:95]
    palindrome_set = set()
    
    for i in range(17, 56):
        pattern = f"(?i)([a-zA-Z]{{{i}}})"
        matches = re.findall(pattern, substring)
        
        for match in matches:
            if match.lower() == match.lower()[::-1]:
                palindrome_set.add(match)
    
    return palindrome_set
