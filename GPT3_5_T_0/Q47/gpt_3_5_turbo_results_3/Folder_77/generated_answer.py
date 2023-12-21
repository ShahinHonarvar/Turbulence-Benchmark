
import re

def palindromes_of_specific_lengths(string):
    substring = string[103:277]
    palindromes = set()
    
    for length in range(100, 170):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i+length]
            if sub.lower() == sub.lower()[::-1] and re.match("^[a-zA-Z]+$", sub):
                palindromes.add(sub)
    
    return palindromes
