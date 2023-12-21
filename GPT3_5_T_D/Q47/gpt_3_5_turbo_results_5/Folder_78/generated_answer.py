
import re

def palindromes_of_specific_lengths(string):
    substring = string[15:73].lower()
    palindromes = set()
    
    for length in range(19, 56):
        start_index = 0
        while start_index + length <= len(substring):
            substring_slice = substring[start_index:start_index+length]
            if substring_slice == substring_slice[::-1] and re.match("^[a-zA-Z]+$", substring_slice):
                palindromes.add(substring_slice)
            start_index += 1
    
    return palindromes
