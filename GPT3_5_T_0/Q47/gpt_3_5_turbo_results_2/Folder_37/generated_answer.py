
import re

def palindromes_of_specific_lengths(string):
    string = string[:10].lower()
    palindromes = set()
    
    for i in range(len(string)-2):
        for j in range(i+3, min(i+6, len(string)+1)):
            substring = string[i:j]
            if re.match("^[a-zA-Z]+$", substring) and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
