
import re

def palindromes_of_specific_lengths(string):
    substring = string[39:95].lower()
    palindromes = set()
    for length in range(14,53):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if re.match('^[a-zA-Z]+$', substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
