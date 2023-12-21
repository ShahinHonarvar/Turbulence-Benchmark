
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)-76):
        substring = string[i:i+77]
        if re.match("^[a-zA-Z]+$", substring) and substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
