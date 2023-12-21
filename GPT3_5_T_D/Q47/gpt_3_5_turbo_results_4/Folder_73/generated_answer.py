
import re

def palindromes_of_specific_lengths(string):
    substring = string[21:63]
    substring = substring.lower()
    palindromes = set()
    
    for length in range(22, 34):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring_slice) and substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)
    
    return palindromes
