
import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{11,}'
    palindromes = set()
    
    for match in re.findall(pattern, string):
        match = match.lower()
        if match == match[::-1]:
            palindromes.add(match)
            
    return palindromes
