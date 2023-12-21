
import re

def palindrome_of_length_n(string):
    palindromes = set()
    n = 464
    string = string.lower()
    length = len(string)
    
    for i in range(length - n + 1):
        substring = string[i:i+n]
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
