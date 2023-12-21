
import re

def palindromes_of_specific_lengths(string):
    substring = string[17:96]
    substring = re.sub("[^a-zA-Z]", "", substring).lower()
    
    palindromes = set()
    
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i+length]
            if substring_slice == substring_slice[::-1]:
                palindromes.add(substring_slice)
                
    return palindromes
