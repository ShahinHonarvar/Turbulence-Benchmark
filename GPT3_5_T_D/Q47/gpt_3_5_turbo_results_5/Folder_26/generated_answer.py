
import re

def palindromes_of_specific_lengths(string):
    substring = string[24:85].lower()
    palindromes = set()
    
    for i in range(len(substring)):
        for j in range(21, 32):
            if i+j <= len(substring) and re.match(r'^[a-zA-Z]+$', substring[i:i+j]):
                if substring[i:i+j] == substring[i:i+j][::-1]:
                    palindromes.add(substring[i:i+j])
    
    return palindromes
