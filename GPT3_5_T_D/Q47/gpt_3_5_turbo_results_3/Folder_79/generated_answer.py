
import re

def palindromes_of_specific_lengths(string):
    substr = string[1:9].lower()
    palindromes = set()
    
    for length in range(3, 5):
        for start in range(len(substr) - length + 1):
            sub = substr[start:start+length]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    
    return palindromes
