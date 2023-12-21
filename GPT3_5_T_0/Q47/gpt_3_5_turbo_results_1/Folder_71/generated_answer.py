
import re

def palindromes_of_specific_lengths(string):
    substring = string[18:66].lower()
    palindromes = set()
    
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1] and re.match("^[a-zA-Z]+$", substring_slice):
                palindromes.add(substring_slice)
    
    return palindromes
