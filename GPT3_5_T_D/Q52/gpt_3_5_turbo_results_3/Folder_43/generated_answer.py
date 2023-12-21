
import re

def palindrome_of_length_n(string):
    string = re.sub(r'[^a-zA-Z]', '', string)
    string = string.lower()
    palindromes = set()
    
    n = len(string)
    l = 51
    
    for i in range(n - l + 1):
        substring = string[i:i + l]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    return palindromes
