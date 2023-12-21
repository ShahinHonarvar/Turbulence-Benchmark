
import re

def palindrome_of_length_n(string):
    palindromes = set()
    n = 416
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if re.match("^[a-zA-Z]+$", substring):
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes
