
import re

def palindromes_of_specific_lengths(string):
    substring = string[18:99].lower()
    palindromes = set()
    
    for length in range(31, 52):
        for i in range(len(substring) - length + 1):
            substring_substr = substring[i:i + length]
            if substring_substr.isalpha() and substring_substr == substring_substr[::-1]:
                palindromes.add(substring_substr)
    
    return palindromes
