
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    length = 95
    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if re.match(r'[a-zA-Z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
