
import re

def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 28):
        substring = string[i:i+29]
        if re.match(r'^[a-z]+$', substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
