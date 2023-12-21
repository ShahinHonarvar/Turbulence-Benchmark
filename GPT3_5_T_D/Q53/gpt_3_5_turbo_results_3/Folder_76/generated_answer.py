
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)-136):
        substring = string[i:i+137]
        if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
            palindromes.add(substring)
    
    return palindromes
