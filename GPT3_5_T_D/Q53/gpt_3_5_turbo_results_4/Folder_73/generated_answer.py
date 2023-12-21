 
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub(r'[^A-Za-z]', '', string)
    string = string.lower()
    palindromes = set()
    n = 94
    
    for i in range(len(string) - n + 1):
        substr = string[i : i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
