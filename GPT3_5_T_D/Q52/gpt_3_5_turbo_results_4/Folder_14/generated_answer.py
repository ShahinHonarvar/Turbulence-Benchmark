
import re

def palindrome_of_length_n(string):
    palindromes = set()
    length = 63
    
    for i in range(len(string) - length + 1):
        substring = string[i:i+length].lower()
        if re.match('^[a-zA-Z]+$', substring) and substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
