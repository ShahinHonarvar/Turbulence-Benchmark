
import re

def palindromes_of_specific_lengths(string):
    substring = string[127:289]
    palindromes = set()
    
    for i in range(len(substring)):
        for length in range(119, 142):
            sub = substring[i:i+length]
            if len(sub) < length:
                break
            if sub.upper() == sub[::-1].upper() and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    
    return palindromes
