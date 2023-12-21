
import re

def palindromes_of_specific_lengths(string):
    substring = string[18:89].lower()

    palindromes = set()
    
    for length in range(12, 15):
        for i in range(0, len(substring) - length + 1):
            temp_str = substring[i:i + length]
            if temp_str == temp_str[::-1] and re.match("^[a-z]*$", temp_str):
                palindromes.add(temp_str)
                
    return palindromes
