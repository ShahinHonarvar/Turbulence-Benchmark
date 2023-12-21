
import re

def palindromes_of_specific_lengths(string):
    substr = string[29:97]
    substr = substr.lower()
    palindromes = set()
    
    for length in range(12, 19):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i+length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
