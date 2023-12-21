
import re

def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    n = 96
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        if re.match(r'^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
