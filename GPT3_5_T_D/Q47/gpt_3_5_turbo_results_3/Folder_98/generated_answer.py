
import re

def palindromes_of_specific_lengths(string):
    string = string[:21].lower()
    palindromes = set()
    for length in range(5, 81):
        for i in range(0, 22 - length):
            substring = string[i:i+length]
            if substring == substring[::-1] and re.match("^[a-zA-Z]+$", substring):
                palindromes.add(substring)
    return palindromes
