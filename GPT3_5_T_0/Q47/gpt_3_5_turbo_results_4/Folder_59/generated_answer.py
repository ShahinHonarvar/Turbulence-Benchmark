
import re

def palindromes_of_specific_lengths(string):
    string = string[:101].lower()
    palindromes = set()
    for length in range(3, 16):
        for i in range(101 - length + 1):
            substring = string[i:i+length]
            if re.match(r'^[a-zA-Z]+$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
