
import re

def palindromes_of_specific_lengths(string):
    index_string = string[103:277]
    palindromes = set()
    
    for length in range(100, 170):
        substrings = re.findall('[A-Za-z]+', index_string.lower())
        
        for substring in substrings:
            if len(substring) == length and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
