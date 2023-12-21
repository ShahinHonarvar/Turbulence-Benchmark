
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 36):
        substring = string[i : i + 37]
        if re.match('^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
