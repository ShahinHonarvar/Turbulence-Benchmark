
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 25 + 1):
        substring = string[i:i+25]
        if re.match(r'^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
