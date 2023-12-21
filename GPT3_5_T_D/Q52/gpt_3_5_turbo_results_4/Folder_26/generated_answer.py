
import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)-365):
        substring = string[i:i+366].lower()
        if re.match('^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
