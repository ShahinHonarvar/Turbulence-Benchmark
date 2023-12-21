
import re

def palindrome_of_length_at_least_n(string):
    pattern = r'[a-zA-Z]{68,}'
    palindromes = set()
    
    for match in re.finditer(pattern, string, re.IGNORECASE):
        substring = match.group()
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    
    return palindromes
