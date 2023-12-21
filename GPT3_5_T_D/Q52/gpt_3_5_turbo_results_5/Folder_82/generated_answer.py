
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    
    for i in range(len(string) - 27):
        substring = string[i:i+28]
        if substring == substring[::-1]:
            palindromes.add(substring)
            
    return palindromes
