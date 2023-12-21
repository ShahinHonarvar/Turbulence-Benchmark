
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[1:9]
    palindromes = set()
    
    for i in range(len(substring)):
        for j in range(i+3, min(i+5, len(substring)+1)):
            sub = substring[i:j]
            if re.match("^[a-zA-Z]+$", sub) and sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
