
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string.lower())
    palindromes = set()
    
    for i in range(len(string) - 38):
        substring = string[i:i+39]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
