
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 254):
        substr = string[i:i+255]
        if re.match(r'^[a-z]+$', substr) and substr == substr[::-1]:
            palindromes.add(substr)
            
    return palindromes
