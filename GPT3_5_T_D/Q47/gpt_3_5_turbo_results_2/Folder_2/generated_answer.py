
import re

def palindromes_of_specific_lengths(text):
    substr = text[10:60].lower()
    palindromes = set()
    
    for length in range(18, 37):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
