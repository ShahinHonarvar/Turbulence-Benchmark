
import re

def palindromes_of_specific_lengths(string):
    substring = string[23:83]
    palindromes = set()
    
    for i in range(len(substring)-1):
        for j in range(i+32, min(i+35, len(substring))):
            sub = substring[i:j+1]
            if sub == sub[::-1] and re.match('^[A-Za-z]+$', sub):
                palindromes.add(sub)
    
    return palindromes
