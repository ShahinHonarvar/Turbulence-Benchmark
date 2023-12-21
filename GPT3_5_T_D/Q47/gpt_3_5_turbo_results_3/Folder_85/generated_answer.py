
import re

def palindromes_of_specific_lengths(string):
    substring = string[29:99]
    substring = substring.lower()
    palindromes = set()
    
    for i in range(len(substring) - 5):
        for length in range(6, 10):
            sub = substring[i:i+length]
            if sub == sub[::-1] and re.match('^[a-zA-Z]+$', sub):
                palindromes.add(sub)
    
    return palindromes
