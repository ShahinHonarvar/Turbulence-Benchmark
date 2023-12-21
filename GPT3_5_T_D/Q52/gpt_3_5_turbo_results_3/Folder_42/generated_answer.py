
import re

def palindrome_of_length_n(string):
    palindromes = set()
    if len(string) < 279:
        return palindromes
    string = string.lower()
    for i in range(len(string)-278):
        substring = string[i:i+279]
        if re.match("^[a-zA-Z]+$", substring):
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
