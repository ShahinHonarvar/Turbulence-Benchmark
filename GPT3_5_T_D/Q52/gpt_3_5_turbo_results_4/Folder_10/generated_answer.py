
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 54
    string = string.lower()
    pattern = r'[a-zA-Z]{%d}' % length
    matches = re.findall(pattern, string)
    
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    
    return palindromes
