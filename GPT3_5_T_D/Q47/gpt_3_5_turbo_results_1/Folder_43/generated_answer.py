
import re

def palindromes_of_specific_lengths(string):
    substring = string[41:90]
    substring = re.sub(r'[^a-zA-Z]', '', substring.lower())
    
    palindromes = set()
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
