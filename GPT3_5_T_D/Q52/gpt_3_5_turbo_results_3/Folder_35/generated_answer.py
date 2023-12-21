
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-115):
        substring = string[i:i+116]
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
