
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 22):
        substring = string[i:i+23]
        if re.match('^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
