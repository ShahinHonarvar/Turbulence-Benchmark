
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    if len(string) < 33:
        return palindromes
    
    for i in range(len(string) - 32):
        substring = string[i:i+33]
        reverse_substring = substring[::-1]
        
        if re.match(r'^[a-zA-Z]+$', substring) and substring == reverse_substring:
            palindromes.add(substring)
    
    return palindromes
