
import re

def palindromes_of_specific_lengths(string):
    substring = string[32:72].lower()
    palindromes = set()
    
    for i in range(21, 33):
        for j in range(len(substring)-i+1):
            sub = substring[j:j+i]
            if re.match('^[a-zA-Z]+$', sub) and sub == sub[::-1]:
                palindromes.add(sub)
                
    return palindromes
