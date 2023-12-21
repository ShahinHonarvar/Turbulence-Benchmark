
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    
    for i in range(len(string) - 6):
        for j in range(i + 6, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
                
    return palindromes
