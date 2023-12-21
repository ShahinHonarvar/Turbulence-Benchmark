
import re

def palindrome_of_length_n(string):
    palindromes = set()
    substring_length = 25
    string = string.lower()
    
    for i in range(len(string) - substring_length + 1):
        substr = string[i:i+substring_length]
        
        if re.match(r'^[a-zA-Z]+$', substr) and substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
