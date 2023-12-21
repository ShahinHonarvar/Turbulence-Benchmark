
import re

def palindromes_of_specific_lengths(string):
    substring = string[62:89].lower()
    palindromes = set()
    
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    
    return palindromes
