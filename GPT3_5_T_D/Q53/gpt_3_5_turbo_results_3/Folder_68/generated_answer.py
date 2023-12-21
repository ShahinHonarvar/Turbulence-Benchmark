
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    substrings = re.findall(r'[a-z]+', string)
    
    for substring in substrings:
        if len(substring) >= 21 and substring == substring[::-1]:
            palindromes.add(substring)
            
    return palindromes
