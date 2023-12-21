
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    if len(string) < 51:
        return palindromes
    
    for i in range(len(string)-50):
        substr = string[i:i+51]
        if re.match("^[a-zA-Z]*$", substr):
            if substr == substr[::-1]:
                palindromes.add(substr)
                
    return palindromes
