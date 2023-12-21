
import re

def palindromes_of_specific_lengths(string):
    substring = string[28:95].lower()
    palindromes = set()
    
    for length in range(38, 50):
        for i in range(len(substring) - length):
            if substring[i:i+length] == substring[i:i+length][::-1] and re.match("^[a-zA-Z]+$", substring[i:i+length]):
                palindromes.add(substring[i:i+length])
    
    return palindromes
