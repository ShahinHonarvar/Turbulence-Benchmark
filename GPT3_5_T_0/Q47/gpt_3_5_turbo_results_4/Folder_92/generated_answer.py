
import re

def palindromes_of_specific_lengths(string):
    string = string[:5].lower()
    palindromes = set()
    
    for i in range(len(string)-2):
        for j in range(i+2, min(i+5, len(string)+1)):
            substring = string[i:j]
            if re.match("^[a-zA-Z]+$", substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    
    return palindromes
