
import re

def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(3, 11):
        for i in range(1, 300 - length):
            substring = string[i:i+length]
            if re.match('^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
