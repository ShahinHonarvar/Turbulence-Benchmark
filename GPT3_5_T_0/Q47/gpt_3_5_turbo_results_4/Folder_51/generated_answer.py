
import re

def palindromes_of_specific_lengths(string):
    substring = string[2:9].lower()
    palindromes = set()
    
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    
    return palindromes
