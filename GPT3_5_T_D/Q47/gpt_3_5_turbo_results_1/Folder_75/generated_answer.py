
import re

def palindromes_of_specific_lengths(string):
    substring = string[31:75]
    palindromes = set()
    
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i+length]
            if candidate.lower() == candidate.lower()[::-1] and re.match("^[a-zA-Z]+$", candidate):
                palindromes.add(candidate)
    
    return palindromes
