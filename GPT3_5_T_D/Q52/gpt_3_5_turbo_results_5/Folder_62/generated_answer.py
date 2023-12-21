
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 187):
        substring = string[i:i+188].lower()
        if re.match(r'^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
