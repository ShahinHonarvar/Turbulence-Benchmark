
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 400):
        substring = string[i:i+401]
        if re.match(r'^[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
