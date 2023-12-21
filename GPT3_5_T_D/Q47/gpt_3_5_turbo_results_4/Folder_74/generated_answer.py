
import re

def palindromes_of_specific_lengths(string):
    substring = string[30:85].lower()
    palindromes = set()

    for length in range(12, 21):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if re.match(r'^[a-z]+$', substr) and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
