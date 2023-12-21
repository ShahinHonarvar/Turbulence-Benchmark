
import re

def palindromes_of_specific_lengths(string):
    substr = string[18:99].lower()
    palindromes = set()
    
    for length in range(31, 52):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i+length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    
    return palindromes
