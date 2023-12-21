
import re

def palindromes_of_specific_lengths(string):
    substring = string[11:88].lower()
    palindromes = set()
    
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
