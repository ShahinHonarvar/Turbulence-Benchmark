
import re

def palindromes_of_specific_lengths(string):
    substring = string[:5].lower()
    palindromes = set()
    
    for length in range(3, 5):
        for start_index in range(5 - length):
            substring_to_check = substring[start_index: start_index + length]
            
            if substring_to_check == substring_to_check[::-1] and re.match('^[a-zA-Z]+$', substring_to_check):
                palindromes.add(substring_to_check)
    
    return palindromes
