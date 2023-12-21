
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string) - 186 + 1):
        substring = string[i: i + 186]
        if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
            palindromes.add(substring)
    
    return palindromes
