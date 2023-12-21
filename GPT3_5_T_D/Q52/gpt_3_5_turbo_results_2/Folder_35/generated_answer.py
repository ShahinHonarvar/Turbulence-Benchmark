
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string).lower()
    palindromes = set()
    
    for i in range(len(string) - 115):
        substring = string[i:i+116]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
