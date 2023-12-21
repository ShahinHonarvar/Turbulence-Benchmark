
import re

def palindromes_of_specific_lengths(string):
    string = string[:7].lower()
    palindromes = set()
    
    for i in range(len(string)):
        for length in range(3, 7):
            substring = string[i:i+length]
            
            if re.match('^[a-z]+$', substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    
    return palindromes
