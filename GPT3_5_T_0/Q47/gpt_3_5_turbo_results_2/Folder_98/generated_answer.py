
import re

def palindromes_of_specific_lengths(string):
    string = string[:21].lower()
    palindromes = set()
    for length in range(5, 81):
        for i in range(21 - length + 1):
            substring = string[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
