
import re

def palindromes_of_specific_lengths(string):
    string = string[:31]
    string = string.lower()
    palindromes = set()
    
    for i in range(len(string)):
        for j in range(20, 31):
            substring = string[i:i+j]
            
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    
    return palindromes
