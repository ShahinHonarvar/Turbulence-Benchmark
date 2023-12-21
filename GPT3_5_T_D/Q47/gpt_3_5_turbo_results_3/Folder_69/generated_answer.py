
import re

def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[11:97].lower()
    
    for length in range(45, 53):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub == sub[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    
    return palindromes
