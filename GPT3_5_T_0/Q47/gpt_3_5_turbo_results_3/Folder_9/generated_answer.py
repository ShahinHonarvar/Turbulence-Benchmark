
import re

def palindromes_of_specific_lengths(string):
    string = string[:301].lower()
    palindromes = set()
    for length in range(50, 61):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
