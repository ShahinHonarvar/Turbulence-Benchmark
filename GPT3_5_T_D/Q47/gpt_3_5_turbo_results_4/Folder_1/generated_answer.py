
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:90].lower()
    palindromes = set()
    
    for length in range(40, 73):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1] and re.match('[a-zA-Z]+$', substr):
                palindromes.add(substr)
    
    return palindromes
