
import re

def palindromes_of_specific_lengths(string):
    substring = string[33:86].lower()
    palindromes = set()
    
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i : i + length]
            if substring_part.isalpha() and substring_part == substring_part[::-1]:
                palindromes.add(substring_part)
    
    return palindromes
