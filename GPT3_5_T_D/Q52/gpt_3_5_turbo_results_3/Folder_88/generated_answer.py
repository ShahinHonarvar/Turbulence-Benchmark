
import re

def palindrome_of_length_n(string):
    n = 13
    string = string.lower()
    string = re.sub(r'[^a-z]', '', string)
    palindromes = set()
    
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
