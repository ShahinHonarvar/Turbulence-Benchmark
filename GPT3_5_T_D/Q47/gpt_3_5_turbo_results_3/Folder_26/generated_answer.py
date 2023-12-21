
import re

def palindromes_of_specific_lengths(string):
    substring = string[24:85].lower()
    palindromes = set()
    
    for length in range(21, 32):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if re.match("^[a-zA-Z]+$", substring_slice) and substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)
    
    return palindromes
