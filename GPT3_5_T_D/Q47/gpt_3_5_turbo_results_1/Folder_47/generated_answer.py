
import re

def palindromes_of_specific_lengths(string):
    substring = string[39:95].lower()
    palindromes = set()
    
    for length in range(14, 53):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1] and re.match(r'^[a-zA-Z]+$', substring_slice):
                palindromes.add(substring_slice)
    
    return palindromes
