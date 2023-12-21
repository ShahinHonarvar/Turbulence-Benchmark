
import re

def palindromes_of_specific_lengths(string):
    substring = string[11:84].lower()
    palindromes = set()
    
    for length in range(13, 67):
        for start in range(83 - length + 1):
            sub = substring[start:start + length]
            if re.match(r'^[a-zA-Z]+$', sub) and sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
