
import re

def palindromes_of_specific_lengths(string):
    substring = string[:301].lower()
    palindromes = set()
    
    for length in range(50, 61):
        for start in range(301 - length):
            sub = substring[start:start+length]
            
            if sub == sub[::-1] and re.match(r'^[a-zA-Z]+$', sub):
                palindromes.add(sub)
    
    return palindromes
