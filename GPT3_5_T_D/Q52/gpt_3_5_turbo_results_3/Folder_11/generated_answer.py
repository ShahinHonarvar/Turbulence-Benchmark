
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    
    for i in range(len(string) - 76):
        substring = string[i:i+77]
        if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
            palindromes.add(substring)
    
    return palindromes
