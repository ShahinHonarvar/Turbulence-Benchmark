
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[18:66]
    palindromes = set()
    
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if re.match('^[a-zA-Z]+$', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
