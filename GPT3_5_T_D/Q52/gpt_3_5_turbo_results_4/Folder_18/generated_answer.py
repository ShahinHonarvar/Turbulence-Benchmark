
import re

def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    
    for i in range(len(s)-391):
        substring = s[i:i+392]
        if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
            palindromes.add(substring)
            
    return palindromes
