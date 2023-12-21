
import re

def palindromes_of_specific_lengths(string):
    substring = string[12:57].lower()
    palindromes = set()
    
    for i in range(len(substring) - 20):
        for j in range(20, 22):
            if re.match(r'^[a-zA-Z]+$', substring[i:i+j]) and substring[i:i+j] == substring[i:i+j][::-1]:
                palindromes.add(substring[i:i+j])
    
    return palindromes
