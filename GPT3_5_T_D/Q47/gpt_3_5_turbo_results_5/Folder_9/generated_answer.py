
import re

def palindromes_of_specific_lengths(chars):
    pattern = r'[A-Za-z]{50,60}'
    substr = chars[:301].lower()
    
    palindromes = set(re.findall(pattern, substr))
    return palindromes
