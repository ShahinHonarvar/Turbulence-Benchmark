
import re

def palindromes_of_specific_lengths(string):
    substring = string[1:9].lower()
    palindromes = set()

    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1] and re.match('^[a-zA-Z]+$', substr):
                palindromes.add(substr)

    return palindromes
