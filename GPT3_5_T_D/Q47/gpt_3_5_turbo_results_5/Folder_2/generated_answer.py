
import re

def palindromes_of_specific_lengths(string):
    substring = string[10:60]
    palindromes = set()
    
    for length in range(18, 37):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i+length]
            if substring_part.isalpha() and substring_part == substring_part[::-1]:
                palindromes.add(substring_part.lower())
    
    return palindromes
