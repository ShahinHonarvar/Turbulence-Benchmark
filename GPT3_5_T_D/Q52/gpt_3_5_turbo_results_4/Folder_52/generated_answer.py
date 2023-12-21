
import re

def palindrome_of_length_n(string):
    palindromes = set()
    n = 423
    string = string.lower()
    
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if re.match("^[a-zA-Z]+$", substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
