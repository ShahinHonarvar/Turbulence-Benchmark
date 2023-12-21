
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)-63):
        substring = string[i:i+64]
        if re.match(r'^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
