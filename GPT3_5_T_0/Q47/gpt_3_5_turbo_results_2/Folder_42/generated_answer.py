
import re

def palindromes_of_specific_lengths(string):
    substring = string[43:96].lower()
    palindromes = set()
    
    for length in range(18, 48):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1] and re.match("^[a-zA-Z]+$", substring_slice):
                palindromes.add(substring_slice)
    
    return palindromes
