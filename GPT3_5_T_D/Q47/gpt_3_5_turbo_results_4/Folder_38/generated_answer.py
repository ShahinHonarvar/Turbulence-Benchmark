
import re

def palindromes_of_specific_lengths(string):
    substring = string[18:88].lower()
    palindromes = set()
    
    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i+length]
            if substring_part == substring_part[::-1] and re.match("^[a-zA-Z]+$", substring_part):
                palindromes.add(substring_part)
    
    return palindromes
