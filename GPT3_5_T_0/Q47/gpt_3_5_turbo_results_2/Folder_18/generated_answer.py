
import re

def palindromes_of_specific_lengths(string):
    substring = string[11:84]
    palindromes = set()
    
    for length in range(13, 67):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub.lower()[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    
    return palindromes
