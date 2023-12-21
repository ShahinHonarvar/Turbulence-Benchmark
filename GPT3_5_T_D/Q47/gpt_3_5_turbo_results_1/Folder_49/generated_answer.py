
import re

def palindromes_of_specific_lengths(string):
    substr = string[10:101].lower()
    palindromes = set()

    for length in range(10, 51):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i+length]
            if substring == substring[::-1] and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)

    return palindromes
